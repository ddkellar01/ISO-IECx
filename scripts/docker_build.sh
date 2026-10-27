#!/usr/bin/env bash
# Local Docker build helper script for ISO-IECx
set -e

IMAGE_NAME="credkellar/iso-iecx"
TAG="${1:-latest}"

echo "Building Docker image ${IMAGE_NAME}:${TAG}..."
docker build -t "${IMAGE_NAME}:${TAG}" .
echo "Build complete: ${IMAGE_NAME}:${TAG}"
