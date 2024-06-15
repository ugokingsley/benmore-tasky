/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'

  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin') /* Flowbite is an open source library of interactive components built on top of Tailwind CSS */
  ],
}

