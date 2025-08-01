# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

All development commands should be run from the root directory:

```bash
bun install              # Install dependencies
bun run docs:dev         # Start development server (http://localhost:5173/resume/)
bun run docs:build       # Build the site for production
bun run docs:preview     # Preview the built site
```

Build output is generated to `docs/.vitepress/dist/` directory.

## Architecture Overview

This is a personal portfolio/resume site built with VitePress and deployed to GitHub Pages:

- **Tech Stack**: Nix (development environment), VitePress (Vue-based static site generator), Bun (runtime), go-task (task runner)
- **Content**: Markdown files in `docs/` directory
- **Configuration**: VitePress config in `docs/.vitepress/config.mts`
- **Deployment**: GitHub Actions workflows deploy to GitHub Pages on master branch pushes
- **Domain**: Managed by Cloudflare

## Key Directory Structure

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
└── bun.lockb              # Bun lock file
```

## Content Organization

- Navigation and sidebar are configured in `docs/.vitepress/config.mts`
- All content is in Markdown format
- Images are stored in `docs/image/` with subdirectories by category
- Site uses local search provider (configured in VitePress config)

## Development Environment

### Quick Start (Recommended: with Nix)

The easiest way to start development:

```bash
nix develop   # Enter Nix development environment (installs bun and go-task)
task start    # Start development server automatically
```

This will start the VitePress development server at `http://localhost:5173/resume/`

### Manual Setup (without Nix)

If you prefer not to use Nix:

```bash
bun install   # Install dependencies
task start    # Start development server
# Or run directly:
bun run docs:dev
```

### Other Task Commands

```bash
task stop    # Stop development environment
```

## CI/CD

- **Build Test**: Runs on PRs to master, only if `docs/**` or other relevant files change
- **Shell Script Validation**: Runs ShellCheck on PRs to master when `script/*.sh` files change
- **Deploy**: Runs on master branch pushes, only if `docs/**` or other relevant files change
- All workflows use Bun and run commands from the root directory