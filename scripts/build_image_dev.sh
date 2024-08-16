#!/bin/bash
set -e
set -o pipefail

source source_env.sh

echo ${DOCKER_REGISTRY_URL}/app_name-devcontainers

# docker build --rm=false -t app_name-devcontainers -t ${DOCKER_REGISTRY_URL}/app_name-devcontainers -f Dockerfile.dev .
docker build --rm=false -t app_name-devcontainers -t hisiter/app_name-devcontainers -f Dockerfile.dev .
docker push hisiter/app_name-devcontainers