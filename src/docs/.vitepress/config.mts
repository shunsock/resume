import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/resume/',
  title: "Shunsuke Tsuchiya",
  description: "Portfolio Site of Shunsuke Tsuchiya",
  themeConfig: {
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Works', link: '/works' },
      { text: 'Resume', link: '/resume' },
      { text: 'Blog', link: '/blog' },
    ],

    sidebar: [
      {
        text: 'Profile',
        items: [
          { text: 'Resume', link: '/resume' },
        ]
      },
      {
        text: 'Works',
        items: [
          { text: 'OSS', link: '/works/oss' },
          { text: 'PR TIMES', link: '/works/prtimes' },
          { text: 'Presentation', link: '/works/presentation' },
        ]
      },
      {
        text: 'Blog',
        items: [
          { text: 'technology', link: '/blog/technology' },
          { text: 'daily', link: '/blog/daily' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/shunsock' }
    ]
  }
})
