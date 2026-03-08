/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './prototype.html',
        './pages/**/*.html',
        './index.html',
    ],
    theme: {
        extend: {
            colors: {
                teal: {
                    50: '#f0fafa', 100: '#d2f0ee', 200: '#a5e0dd',
                    300: '#7ecec5', 400: '#54b5aa', 500: '#479793',
                    600: '#387a77', 700: '#2d5e5b', 800: '#234a48',
                    900: '#1a3836', 950: '#0f2322'
                },
                mint: {
                    50: '#edfcf8', 100: '#d4f7ee', 200: '#a8eedc',
                    300: '#6ee0c5', 400: '#3dcbaa', 500: '#12ad98',
                    600: '#0e8b7a', 700: '#0f6f63', 800: '#115850',
                    900: '#114943'
                },
                gold: {
                    50: '#fffceb', 100: '#fef6c7', 200: '#fdec8a',
                    300: '#fcdc4d', 400: '#fad500', 500: '#d4a01c',
                    600: '#b47d15', 700: '#8f5d14', 800: '#774a18',
                    900: '#633d1a'
                },
                cream: {
                    50: '#fefdfb', 100: '#fdfaf3', 200: '#faf5e8',
                    300: '#f5edd5', 400: '#ede0b8', 500: '#e2cf99'
                },
                slate: {
                    700: '#374151', 800: '#1f2937', 900: '#111827'
                },
            },
            fontFamily: {
                serif: ['"DM Serif Display"', 'Georgia', 'serif'],
                sans: ['"Source Sans 3"', 'system-ui', 'sans-serif'],
            },
        }
    },
    plugins: [],
}
