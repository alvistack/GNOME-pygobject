#!/bin/bash

set -e

TAG="registry.gitlab.gnome.org/gnome/pygobject/main:v17"

sudo docker build --build-arg HOST_USER_ID="$UID" --tag "${TAG}" \
    --file "Dockerfile" .
sudo docker run -e PYENV_VERSION='3.8.12-debug' --rm --security-opt label=disable \
    --volume "$(pwd)/..:/home/user/app" --workdir "/home/user/app" \
    --tty --interactive "${TAG}" bash
