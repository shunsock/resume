import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/resume/',
  title: "Shunsuke.Tsuchiya",
  description: "Resume and Portfolio",
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
        text: 'Works',
        items: [
          { text: 'OSS', link: '/works/oss' },
          { text: 'PR TIMES', link: '/works/prtimes' },
          { text: 'Presentation', link: '/works/presentation' },
        ]
      },
      {
        text: 'Resume',
        link: '/resume',
      },
      {
        text: 'Blog',
        link: '/blog',
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/shunsock' }
    ]
  }
})
