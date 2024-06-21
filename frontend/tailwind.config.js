/** @type {import('tailwindcss').Config} */
export default {
    darkMode: 'selector',
    // darkMode: 'media',
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx,vue}",
        "./src/*.{js,ts,jsx,tsx,vue}",
        "./node_modules/flowbite/**/*.js",
    ],
    theme: {
        fontFamily: {
            sans: ["Roboto", "Helvetica", "Arial", "sans-serif"],
        },
        extend: {
            colors: {
                "primary": {
                    50: "#eef2ff",
                    100: "#e0e7ff",
                    200: "#c7d2fe",
                    300: "#a5b4fc",
                    400: "#818cf8",
                    500: "#6366f1",
                    600: "#4f46e5",
                    700: "#4338ca",
                    800: "#3730a3",
                    900: "#312e81",
                    950: "#1e1b4b",
                }
            },
            contrast: {
                95: '.95',
            }
        },
    },
    plugins: [
        require('flowbite/plugin')
    ],
}

