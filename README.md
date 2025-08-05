# Resume Site

![](./docs/public/profile/shunsuke_tsuchiya.jpg)

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

## Architecture Overview

This is a personal portfolio/resume site built with VitePress and deployed to GitHub Pages:

- **Tech Stack**: Nix (development environment), VitePress (Vue-based static site generator), Bun (runtime), go-task (task runner)
- **Content**: Markdown files in `docs/` directory
- **Configuration**: VitePress config in `docs/.vitepress/config.mts`
- **Deployment**: GitHub Actions workflows deploy to GitHub Pages on master branch pushes
- **Domain**: Managed by Cloudflare
- **Build Output**: Generated to `docs/.vitepress/dist/` directory

## Development Commands

All development commands should be run from the root directory:

```bash
bun install              # Install dependencies
bun run docs:dev         # Start development server (http://localhost:5173/resume/)
bun run docs:build       # Build the site for production
bun run docs:preview     # Preview the built site
```

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

4. Open your browser and visit `http://localhost:5173/`


## CI/CD

### Build

The `.github/workflows/build.yml` workflow is triggered when a pull request is opened against the master branch. This workflow only runs if changes are made within the `docs` directory or other relevant files.

The build process is significant as it performs dead link checking to ensure all internal and external links remain functional before merging changes.

### Code Review

GitHub Copilot is configured with review guidelines in `.github/copilot-instructions.md` to provide automated code review feedback. The review process focuses on:

- **Japanese content**: Readability, consistency, and clarity of markdown content
- **Shell scripts**: Best practices, style consistency, flexibility, and robustness
- **Taskfile**: Task naming consistency and proper descriptions
- **Nix configuration**: Following Nix best practices and style consistency

Review feedback is categorized as `[must]` (critical changes), `[nits]` (improvement suggestions), or `[question]` (clarification requests).

### Shell Script Validation

The `.github/workflows/validate_shellscript.yml` workflow runs ShellCheck validation on shell scripts in the `script/` directory when pull requests modify any `.sh` files. This ensures shell script quality and catches common scripting issues before merge.

### Deploy

The `.github/workflows/deploy.yml` workflow is triggered when changes are pushed to the master branch. Similar to the CI workflow, deployment only proceeds if there are changes detected in the relevant directories.

## Content Organization

- Navigation and sidebar are configured in `docs/.vitepress/config.mts`
- All content is in Markdown format
- Images are stored in `docs/image/` with subdirectories by category
- Site uses local search provider (configured in VitePress config)

## Project Structure

```
resume/
├── .github/                # GitHub Actions workflows and configs
├── docs/                   # All content and configuration
│   ├── .vitepress/         # VitePress configuration
│   │   └── config.mts      # Main site configuration
│   ├── blog/               # Blog posts (technology, daily)
│   ├── profile/            # Profile info, resume, skills
│   ├── works/              # Work projects (Findy, PR TIMES, presentations)
│   ├── image/              # Static assets
│   └── index.md            # Homepage
├── script/                 # Development scripts
├── flake.nix               # Nix development environment
├── flake.lock              # Nix lock file
├── Taskfile.yml            # Task runner configuration
├── package.json            # Dependencies and scripts
├── bun.lockb               # Bun lock file
└── README.md               # This file
```

## License

[MIT](LICENSE)

