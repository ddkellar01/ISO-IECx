#!/usr/bin/env bash
# Docker Hub publishing script for ISO-IECx
set -e

IMAGE_NAME="credkellar/iso-iecx"
TAG="${1:-latest}"

echo "Logging in to Docker Hub..."
docker login

echo "Building production image..."
docker build -t "${IMAGE_NAME}:${TAG}" -t "${IMAGE_NAME}:latest" .

echo "Pushing image to Docker Hub..."
docker push "${IMAGE_NAME}:${TAG}"
docker push "${IMAGE_NAME}:latest"

echo "Successfully published ${IMAGE_NAME}:${TAG} and latest to Docker Hub!"
