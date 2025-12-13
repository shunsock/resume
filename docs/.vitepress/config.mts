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
      { text: 'ホーム', link: '/' },
      { text: '経歴', link: '/resume' },
      { text: '能力・技術', link: '/skill' },
      { text: '開発事例', link: '/project' },
      { text: '登壇', link: '/presentation' },
      { text: '投稿・寄稿', link: '/blog' },
    ],

    sidebar: [
      {
        text: '経歴',
        items: [
          { text: '職務経歴書', link: '/resume' },
        ]
      },
      {
        text: '能力・技術',
        items: [
          { text: 'スキル一覧', link: '/skill' },
        ]
      },
      {
        text: '開発事例',
        items: [
          { text: 'Findy', link: '/project/findy' },
          { text: 'PR TIMES', link: '/project/prtimes' },
        ]
      },
      {
        text: '登壇',
        items: [
          { text: '登壇', link: '/presentation' },
        ]
      },
      {
        text: '投稿・寄稿',
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
