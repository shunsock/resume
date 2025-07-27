#!/bin/bash

# Entry point script for VitePress development
# This script sets up the development environment and starts the dev server

set -euo pipefail

echo "🚀 Starting VitePress development environment..."

# Navigate to the source directory
cd /usr/vitepress/src

echo "📦 Installing dependencies with Bun..."
bun install

echo "🔧 Starting VitePress development server..."
echo "   -> Server will be available at http://localhost:5173/resume/"
echo "   -> Press Ctrl+C to stop the server"

# Start the development server
bun run docs:dev
