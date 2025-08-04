#!/bin/bash

set -euo pipefail

[ -d "node_modules" ] && rm -rf -- "node_modules"
bun install
bun run docs:build

