"""Render a draw.io (mxGraphModel) flowchart to a self-contained SVG.

Handles the subset the TropicalNotes algorithms use: rounded/plain rects,
text cells, orthogonal edges with exit/entry hints and optional waypoints,
HTML labels with <b>/<br>/<font>, dashed strokes and edge labels.
"""
import xml.etree.ElementTree as ET
import html as htmlmod
import re, sys

FONT = "'Source Sans 3', 'Segoe UI', system-ui, sans-serif"
PAD = 24


def parse_style(s):
    d = {}
    for kv in (s or '').split(';'):
        if not kv:
            continue
        if '=' in kv:
            k, v = kv.split('=', 1)
            d[k] = v
        else:
            d[kv] = True
    return d


def label_lines(value):
    """HTML label -> list of (text, bold) line segments."""
    if not value:
        return []
    v = value.replace('\n', ' ')
    v = re.sub(r'<br\s*/?>', '\n', v, flags=re.I)
    v = re.sub(r'</div>|</p>', '\n', v, flags=re.I)
    out = []
    for raw in v.split('\n'):
        # bold if the whole segment sits in <b>/<strong>, or font-weight:bold
        bold = bool(re.search(r'<(b|strong)>', raw, re.I))
        if re.search(r'font-weight:\s*normal', raw, re.I):
            bold = False
        txt = re.sub(r'<[^>]+>', '', raw)
        txt = htmlmod.unescape(txt).strip()
        if txt:
            out.append((txt, bold))
    return out


def wrap(text, width_px, font_px):
    """Greedy wrap using an average glyph width."""
    per = font_px * 0.52
    maxc = max(int(width_px / per), 6)
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if len(t) <= maxc:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def convert(path, out_path, title):
    root = ET.parse(path).getroot()
    cells = root.findall('.//mxCell')
    V = {}
    order = []
    for c in cells:
        g = c.find('mxGeometry')
        st = parse_style(c.get('style'))
        if c.get('vertex') == '1' and g is not None:
            V[c.get('id')] = dict(
                x=float(g.get('x') or 0), y=float(g.get('y') or 0),
                w=float(g.get('width') or 0), h=float(g.get('height') or 0),
                style=st, value=c.get('value') or '')
            order.append(c.get('id'))

    # bounds
    xs = [v['x'] for v in V.values()] + [v['x'] + v['w'] for v in V.values()]
    ys = [v['y'] for v in V.values()] + [v['y'] + v['h'] for v in V.values()]
    minx, maxx, miny, maxy = min(xs) - PAD, max(xs) + PAD, min(ys) - PAD, max(ys) + PAD
    W, H = maxx - minx, maxy - miny

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{minx:.0f} {miny:.0f} {W:.0f} {H:.0f}" '
        f'width="100%" role="img" aria-label="{esc(title)}" font-family="{FONT}">')
    parts.append(f'<title>{esc(title)}</title>')
    parts.append('<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
                 'markerWidth="7" markerHeight="7" orient="auto-start-end">'
                 '<path d="M0,0 L10,5 L0,10 z" fill="#5a6b73"/></marker></defs>')
    parts.append(f'<rect x="{minx:.0f}" y="{miny:.0f}" width="{W:.0f}" height="{H:.0f}" fill="#ffffff"/>')

    def anchor(vid, sx, sy, dx, dy, other):
        """Connection point on a vertex: explicit exit/entry, else nearest side."""
        v = V[vid]
        if sx is not None:
            return (v['x'] + float(sx) * v['w'] + float(dx or 0),
                    v['y'] + float(sy) * v['h'] + float(dy or 0))
        ocx, ocy = other['x'] + other['w'] / 2, other['y'] + other['h'] / 2
        cx, cy = v['x'] + v['w'] / 2, v['y'] + v['h'] / 2
        if abs(ocy - cy) >= abs(ocx - cx):
            return (cx, v['y'] + v['h'] if ocy > cy else v['y'])
        return (v['x'] + v['w'] if ocx > cx else v['x'], cy)

    # ---- edges (drawn beneath shapes) ----
    for c in cells:
        if c.get('edge') != '1':
            continue
        s, t = c.get('source'), c.get('target')
        if s not in V or t not in V:
            continue
        st = parse_style(c.get('style'))
        g = c.find('mxGeometry')
        pts = [(float(p.get('x')), float(p.get('y')))
               for p in (g.findall("./Array[@as='points']/mxPoint") if g is not None else [])]
        p0 = anchor(s, st.get('exitX'), st.get('exitY'), st.get('exitDx'), st.get('exitDy'), V[t])
        p1 = anchor(t, st.get('entryX'), st.get('entryY'), st.get('entryDx'), st.get('entryDy'), V[s])

        route = [p0] + pts + [p1]
        d = f"M {route[0][0]:.1f} {route[0][1]:.1f}"
        for i in range(1, len(route)):
            ax, ay = route[i - 1]
            bx, by = route[i]
            if abs(ax - bx) < 0.5 or abs(ay - by) < 0.5:
                d += f" L {bx:.1f} {by:.1f}"                      # already straight
            elif i == 1 and not pts:
                # single orthogonal dog-leg; direction from the exit side
                if abs(by - ay) >= abs(bx - ax):
                    my = (ay + by) / 2
                    d += f" L {ax:.1f} {my:.1f} L {bx:.1f} {my:.1f} L {bx:.1f} {by:.1f}"
                else:
                    mx = (ax + bx) / 2
                    d += f" L {mx:.1f} {ay:.1f} L {mx:.1f} {by:.1f} L {bx:.1f} {by:.1f}"
            else:
                d += f" L {bx:.1f} {ay:.1f} L {bx:.1f} {by:.1f}"
        stroke = st.get('strokeColor', '#5a6b73')
        if stroke in ('none', None):
            stroke = '#5a6b73'
        sw = st.get('strokeWidth', '1.6')
        dash = ' stroke-dasharray="7 4"' if st.get('dashed') == '1' else ''
        parts.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"{dash} '
                     f'marker-end="url(#arrow)" stroke-linejoin="round"/>')

        lab = label_lines(c.get('value'))
        if lab:
            mx = sum(p[0] for p in route) / len(route)
            my = sum(p[1] for p in route) / len(route)
            fs = float(st.get('fontSize', 13))
            txt = ' '.join(t for t, _ in lab)
            wpx = len(txt) * fs * 0.52 + 10
            parts.append(f'<rect x="{mx - wpx/2:.1f}" y="{my - fs*0.85:.1f}" width="{wpx:.1f}" '
                         f'height="{fs*1.7:.1f}" rx="4" fill="#ffffff" fill-opacity="0.92"/>')
            parts.append(f'<text x="{mx:.1f}" y="{my:.1f}" font-size="{fs:.0f}" fill="'
                         f'{st.get("fontColor", "#40525c")}" text-anchor="middle" '
                         f'dominant-baseline="central">{esc(txt)}</text>')

    # ---- vertices ----
    for vid in order:
        v = V[vid]
        st, x, y, w, h = v['style'], v['x'], v['y'], v['w'], v['h']
        is_text = 'text' in st and st.get('fillColor') in (None, 'none')
        fill = st.get('fillColor', 'none' if is_text else '#ffffff')
        stroke = st.get('strokeColor', 'none')
        fs = float(st.get('fontSize', 16))
        fc = st.get('fontColor', '#1a3836')
        if not is_text:
            rx = min(float(st.get('arcSize', 10)) / 2.0, min(w, h) / 2) if st.get('rounded') == '1' else 0
            dash = ' stroke-dasharray="8 4"' if st.get('dashed') == '1' else ''
            sattr = '' if stroke == 'none' else f' stroke="{stroke}" stroke-width="{st.get("strokeWidth", 1.5)}"'
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
                         f'rx="{rx:.1f}" fill="{fill}"{sattr}{dash}/>')

        segs = label_lines(v['value'])
        if not segs:
            continue
        # shrink the font until the wrapped label fits inside the shape
        lines = []
        while True:
            lines = []
            for txt, bold in segs:
                for ln in wrap(txt, w - 14, fs):
                    lines.append((ln, bold))
            if is_text or len(lines) * fs * 1.25 <= h - 6 or fs <= 9:
                break
            fs -= 1
        lh = fs * 1.25
        total = len(lines) * lh
        va = st.get('verticalAlign', 'middle')
        top = y + 6 if va == 'top' else y + (h - total) / 2
        al = st.get('align', 'center')
        if al == 'left':
            tx, anch = x + 8 + float(st.get('spacingLeft', 0) or 0), 'start'
        elif al == 'right':
            tx, anch = x + w - 8, 'end'
        else:
            tx, anch = x + w / 2, 'middle'
        for i, (ln, bold) in enumerate(lines):
            ty = top + lh * (i + 0.78)
            fw = ' font-weight="700"' if (bold or st.get('fontStyle') in ('1', '3')) else ''
            parts.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="{fs:.0f}" fill="{fc}" '
                         f'text-anchor="{anch}"{fw}>{esc(ln)}</text>')

    parts.append('</svg>')
    open(out_path, 'w', encoding='utf-8').write('\n'.join(parts))
    print(f"  {out_path}  ({len(V)} shapes, {len('|'.join(parts))} bytes)")


if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2], sys.argv[3])
