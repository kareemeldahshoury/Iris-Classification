import type { Config } from 'tailwindcss';

export default {
  content: [
    './src/**/*.{html,js,svelte,ts}', // Matches all relevant files in `src`
    './app.html',                     // Includes `app.html` for Tailwind classes
  ],
  theme: {
    extend: {},
  },
  plugins: [],
} satisfies Config;
