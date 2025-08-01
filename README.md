# Resume Site

![](./docs/image/profile/shunsuke_tsuchiya.jpg)

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
- GitHub: [https://github.com/shunsock/resume/tree/master/docs](https://github.com/shunsock/resume/tree/master/docs)
- Local files: Browse the content directly in the `docs/` directory

## Tech Stack

- [Nix](https://nixos.org/) - Development environment management
- [VitePress](https://vitepress.dev/) - Static site generator based on Vue
- [Bun](https://bun.sh/) - JavaScript runtime and package manager
- [go-task](https://taskfile.dev/) - Task runner
- [GitHub Actions](https://github.com/features/actions) for CI/CD
- [GitHub Pages](https://pages.github.com/) for hosting
- [Clouflare](https://www.cloudflare.com/) for mangaging domain

## Development

### Quick Start (Recommended: with Nix)

1. Clone the repository
   ```bash
   git clone https://github.com/shunsock/resume.git
   cd resume
   ```

2. Enter Nix development environment (automatically installs bun and go-task)
   ```bash
   nix develop
   ```

3. Start the development server
   ```bash
   task start
   ```

4. Open your browser and visit `http://localhost:5173/resume/`

### Manual Setup (without Nix)

If you prefer not to use Nix:

1. Install dependencies manually:
   - [Bun](https://bun.sh/) - JavaScript runtime and package manager
   - [go-task](https://taskfile.dev/) - Task runner

2. Install project dependencies
   ```bash
   bun install
   ```

3. Start the development server
   ```bash
   task start
   # Or run directly:
   bun run docs:dev
   ```

4. Open your browser and visit `http://localhost:5173/resume/`


## CI/CD

### CI

The `.github/workflows/build.yml` workflow is triggered when a pull request is opened against the master branch. Please note that the deployment workflow only runs if changes are made within the `docs` directory or other relevant files.

### Shell Script Validation

The `.github/workflows/validate_shellscript.yml` workflow runs ShellCheck validation on shell scripts in the `script/` directory when pull requests modify any `.sh` files. This ensures shell script quality and catches common scripting issues before merge.

### Deploy

The `.github/workflows/deploy.yml` workflow is triggered when changes are pushed to the master branch. Similar to the CI workflow, deployment only proceeds if there are changes detected in the relevant directories.

## Project Structure

```
resume/
├── .github/                # GitHub Actions workflows and configs
├── docs/                   # Content files (Markdown)
│   ├── .vitepress/         # VitePress configuration
│   ├── blog/               # Blog posts
│   ├── profile/            # Profile information
│   ├── works/              # Work projects
│   └── index.md            # Home page
├── script/                 # Development scripts
├── flake.nix               # Nix development environment
├── flake.lock              # Nix lock file
├── Taskfile.yml            # Task runner configuration
├── bun.lockb               # Bun lock file
├── package.json            # Project dependencies and scripts
└── README.md               # This file
```

## License

[MIT](LICENSE)

