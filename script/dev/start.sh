#!/bin/bash

set -euo pipefail

docker compose up -d --build
docker compose exec vitepress ./entry_point.sh
