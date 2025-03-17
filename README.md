# Resume Site

![](./src/docs/image/profile/shunsock_icon.jpeg)

This is a personal portfolio and resume site for Shunsuke Tsuchiya, built with VitePress and deployed to GitHub Pages.

## Project Overview

This site contains:
- Personal profile and self-introduction
- Resume and career history
- Showcase of work projects and open-source software
- List of presentations at conferences
- Technical and personal blog posts

You can view this resume site at:
- GitHub Pages: [https://shunsock.github.io/resume/](https://shunsock.github.io/resume/)
- GitHub: [https://github.com/shunsock/resume/tree/master/src/docs](https://github.com/shunsock/resume/tree/master/src/docs)
- Local files: Browse the content directly in the `src/docs/` directory

## Tech Stack

- [VitePress](https://vitepress.dev/) - Static site generator based on Vue
- [Bun](https://bun.sh/) - JavaScript runtime and package manager
- GitHub Actions for CI/CD
- GitHub Pages for hosting

## Development

### Prerequisites

- [Bun](https://bun.sh/) (v1.0.11 or later)

### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/shunsock/resume.git
   cd resume/src
   ```

2. Install dependencies
   ```bash
   bun install
   ```

3. Start the development server
   ```bash
   bun run docs:dev
   ```

4. Open your browser and visit `http://localhost:5173/resume/`

## Building for Production

```bash
cd src
bun run docs:build
```

The built site will be available in `src/docs/.vitepress/dist`.

## Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the `master` branch. The deployment is handled by a GitHub Actions workflow defined in `.github/workflows/deploy.yml`.

## Project Structure

```
resume/
├── .github/                # GitHub Actions workflows and configs
├── src/                    # Source code
│   ├── docs/               # Content files (Markdown)
│   │   ├── .vitepress/     # VitePress configuration
│   │   ├── blog/           # Blog posts
│   │   ├── profile/        # Profile information
│   │   ├── works/          # Work projects
│   │   └── index.md        # Home page
│   ├── bun.lockb           # Bun lock file
│   └── package.json        # Project dependencies and scripts
└── README.md               # This file
```

## License

[MIT](LICENSE)
