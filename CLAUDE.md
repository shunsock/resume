# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

All development commands should be run from the `src/` directory:

```bash
cd src
bun install              # Install dependencies
bun run docs:dev         # Start development server (http://localhost:5173/resume/)
bun run docs:build       # Build the site for production
bun run docs:preview     # Preview the built site
```

## Architecture Overview

This is a personal portfolio/resume site built with VitePress and deployed to GitHub Pages:

- **Tech Stack**: VitePress (Vue-based static site generator) + Bun runtime
- **Content**: Markdown files in `src/docs/` directory
- **Configuration**: VitePress config in `src/docs/.vitepress/config.mts`
- **Deployment**: GitHub Actions workflows deploy to GitHub Pages on master branch pushes

## Key Directory Structure

```
src/
├── docs/                    # All content and configuration
│   ├── .vitepress/         # VitePress configuration
│   │   └── config.mts      # Main site configuration
│   ├── blog/               # Blog posts (technology, daily)
│   ├── profile/            # Profile info, resume, skills
│   ├── works/              # Work projects (Findy, PR TIMES, presentations)
│   ├── image/              # Static assets
│   └── index.md            # Homepage
├── package.json            # Dependencies and npm scripts
└── bun.lockb              # Bun lock file
```

## Content Organization

- Navigation and sidebar are configured in `src/docs/.vitepress/config.mts`
- All content is in Markdown format
- Images are stored in `src/docs/image/` with subdirectories by category
- Site uses local search provider (configured in VitePress config)

## Development Environment

The project supports Docker development:
- `docker compose up -d --build` - Build and start container
- `docker compose exec vitepress bash` - Enter container
- Then run bun commands from within the container

## CI/CD

- **Build Test**: Runs on PRs to master, only if `src/**` files change
- **Deploy**: Runs on master branch pushes, only if `src/**` files change
- Both workflows use Bun 1.0.11 and run commands from `src/` directory