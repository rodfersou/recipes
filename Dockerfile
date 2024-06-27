# syntax=docker/dockerfile:1
FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV PATH="/nix/var/nix/profiles/default/bin:$PATH" \
    INSIDE_DOCKER="true"
# fly.io don't support multiple volumes
ENV POETRY_CACHE_DIR="/nix/poetry"

COPY . /app
WORKDIR /app

RUN <<DOCKER_BEFORE   bash                                                          \
 && <<CONFIG_NIX_CONF sed -r 's/^ {4}//;/^$/d;/^#/d' | cat > ~/.config/nix/nix.conf \
 && <<DOCKER_AFTER    bash

# DOCKER BEFORE
    apt update -y
    apt install -y \
        curl
    mkdir -p ~/.config/nix
DOCKER_BEFORE

# CONFIG NIX_CONF
    experimental-features = nix-command flakes
    filter-syscalls = false
CONFIG_NIX_CONF

# DOCKER AFTER
    # NIX
    curl --proto '=https'                           \
         --tlsv1.2                                  \
         -sSf                                       \
         -L https://install.determinate.systems/nix \
    | sh -s                                         \
         -- install linux                           \
         --extra-conf "sandbox = false"             \
         --extra-conf "filter-syscalls = false"     \
         --init none                                \
         --no-confirm

    # CLEAN
    nix-collect-garbage -d
    apt-get clean
    apt-get autoremove -y
    rm -rf /var/lib/apt/lists/*
DOCKER_AFTER
CMD ["./scripts/start-prod"]
