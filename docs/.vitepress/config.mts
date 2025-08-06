import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/',
  title: "Shunsuke Tsuchiya",
  head: [
    [
      'link',
      {
        rel: 'icon',
        type: 'image/jpeg',
        href: 'https://avatars.githubusercontent.com/u/84004458?s=96&v=4',
      }
    ]
  ],
  description: "Portfolio Site of Shunsuke Tsuchiya",
  themeConfig: {
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Resume', link: '/resume' },
      { text: 'Project', link: '/project' },
      { text: 'Presentation', link: '/presentation' },
      { text: 'Blog', link: '/blog' },
    ],

    sidebar: [
      {
        text: 'Resume',
        items: [
          { text: 'Resume', link: '/resume' },
          { text: 'Skills', link: '/resume/skills' },
        ]
      },
      {
        text: 'Project',
        items: [
          { text: 'Findy', link: '/project/findy' },
          { text: 'PR TIMES', link: '/project/prtimes' },
        ]
      },
      {
        text: 'Presentation',
        items: [
          { text: 'Presentation', link: '/presentation' },
        ]
      },
      {
        text: 'Blog',
        items: [
          { text: 'Findy', link: '/blog/findy' },
          { text: 'Findy Tech Blog', link: '/blog/findy_techblog' },
          { text: 'はてなブログ', link: '/blog/hatena_blog' },
          { text: '集まれ統計の森', link: '/blog/hello_statisticians' },
          { text: 'note', link: '/blog/note' },
          { text: 'PR TIMES開発者ブログ', link: '/blog/prtimes_techblog' },
          { text: 'Zenn', link: '/blog/zenn' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/shunsock' }
    ]
  }
})
