import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/resume/',
  title: "Shunsuke Tsuchiya",
  head: [
  ['link', { rel: 'icon', type: 'image/jpeg', href: '/resume/image/profile/shunsock_icon.jpeg' }]
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
          { text: 'Self Introduction', link: '/profile/introduction' },
          { text: 'Resume', link: '/profile/resume' },
        ]
      },
      {
        text: 'Works',
        items: [
          { text: 'OSS', link: '/works/oss' },
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
