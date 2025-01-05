import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/resume/',
  title: "Shunsuke.Tsuchiya",
  description: "Resume and Portfolio",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Profile', link: '/profile' },
      { text: 'Resume', link: '/resume' },
      { text: 'Portfolio', link: '/portfolio' },
      { text: 'Blog', link: '/blog' },
    ],

    sidebar: [
      {
        text: 'Items',
        items: [
          { text: 'Profile', link: '/profile' },
          { text: 'Resume', link: '/resume' },
          { text: 'Portfolio', link: '/portfolio' },
          { text: 'Blog', link: '/blog' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
