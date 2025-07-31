import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/',
  title: "Shunsuke Tsuchiya",
  head: [
  ['link', { rel: 'icon', type: 'image/jpeg', href: 'https://avatars.githubusercontent.com/u/84004458?s=96&v=4' }]
],
  description: "Portfolio Site of Shunsuke Tsuchiya",
  themeConfig: {
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Profile', link: '/profile' },
      { text: 'Works', link: '/works' },
      { text: 'Blog', link: '/blog' },
    ],

    sidebar: [
      {
        text: 'Profile',
        items: [
          { text: 'Resume', link: '/profile/resume' },
          { text: 'Skills', link: '/profile/skills' },
        ]
      },
      {
        text: 'Works',
        items: [
          { text: 'Findy', link: '/works/findy' },
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
