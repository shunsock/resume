#!/bin/bash

set -euo pipefail

[ -d "node_modules" ] && rm -rf -- "node_modules"
bun run docs:dev

