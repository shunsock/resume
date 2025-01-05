import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/resume/',
  title: "Shunsuke.Tsuchiya (@shunsock)",
  description: "Resume and Portfolio",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Profile', link: '/profile' },
      { text: 'Blog', link: '/blog' },
      { text: 'Resume', link: '/resume' },
    ],

    sidebar: [
      {
        text: 'Pages',
        items: [
          { text: 'Profile', link: '/profile' },
          { text: 'Blog', link: '/blog' },
          { text: 'Resume', link: '/resume' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
