#!/usr/bin/env bash
# Docker Hub publishing script for ISO-IECx using DOCKERHUB_USERNAME and DOCKERHUB_TOKEN
set -e

IMAGE_NAME="credkellar/iso-iecx"
TAG="${1:-latest}"

if [ -z "$DOCKERHUB_USERNAME" ] || [ -z "$DOCKERHUB_TOKEN" ]; then
    echo "Error: DOCKERHUB_USERNAME and DOCKERHUB_TOKEN environment variables must be set."
    exit 1
fi

echo "Logging in to Docker Hub as $DOCKERHUB_USERNAME..."
echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

echo "Building production image..."
docker build -t "${IMAGE_NAME}:${TAG}" -t "${IMAGE_NAME}:latest" .

echo "Pushing image to Docker Hub..."
docker push "${IMAGE_NAME}:${TAG}"
docker push "${IMAGE_NAME}:latest"

echo "Successfully published ${IMAGE_NAME}:${TAG} and latest to Docker Hub!"
