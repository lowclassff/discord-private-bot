
## File: `install.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

# install.sh - simple helper to build and run docker locally for development
if [ ! -f .env ]; then
  echo ".env not found. Copy .env.example to .env and edit it." >&2
  exit 1
fi

IMAGE_NAME=discord-vps-bot
DOCKERFILE=Dockerfile1

echo "Building Docker image $IMAGE_NAME using $DOCKERFILE..."
docker build -t "$IMAGE_NAME" -f "$DOCKERFILE" .

echo "Run with: docker run --env-file .env --rm $IMAGE_NAME"
