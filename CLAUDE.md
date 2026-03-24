# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

All development commands should be run from the root directory:

```bash
nix run                  # Start development server (auto-installs deps, http://localhost:5173/resume/)
nix run .#build          # Build the site for production (auto-installs deps)
task run                 # Same as nix run (via script/run.sh)
task build               # Same as nix run .#build (via script/build.sh)
```

`nix run` apps automatically clean `node_modules` and run `bun install` before starting.

Build output is generated to `docs/.vitepress/dist/` directory.

## Architecture Overview

This is a personal portfolio/resume site built with VitePress and deployed to GitHub Pages:

- **Tech Stack**: Nix (development environment & app runner), VitePress (Vue-based static site generator), Bun (runtime), go-task (task runner)
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
├── flake.nix               # Nix development environment
├── flake.lock              # Nix lock file
├── Taskfile.yml            # Task runner configuration
├── script/                 # Shell scripts for task runner
│   ├── run.sh              # Runs nix run (dev server)
│   └── build.sh            # Runs nix run .#build (production build)
├── package.json            # Dependencies and scripts
└── bun.lock               # Bun lock file
```

## Content Organization

- Navigation and sidebar are configured in `docs/.vitepress/config.mts`
- All content is in Markdown format
- Images are stored in `docs/image/` with subdirectories by category
- Site uses local search provider (configured in VitePress config)

## Development Environment

### Quick Start (Recommended)

One command to start the development server:

```bash
nix run       # Cleans node_modules, installs deps, starts dev server
```

Or equivalently via go-task:

```bash
nix develop   # Enter Nix devShell (provides bun and go-task)
task run      # Delegates to script/run.sh → nix run
```

This will start the VitePress development server at `http://localhost:5173/resume/`

### Build

```bash
nix run .#build   # Production build (or: task build)
```

## CI/CD

- **Build Test**: Runs on PRs to master, only if `docs/**` or other relevant files change
- **Deploy**: Runs on master branch pushes, only if `docs/**` or other relevant files change
- All workflows use Nix (`cachix/install-nix-action`) and run `bash script/build.sh` (`nix run .#build`)