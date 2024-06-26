FROM nixos/nix:latest AS builder
ENV INSIDE_DOCKER="true"
COPY . /tmp/build
WORKDIR /tmp/build
RUN nix                                                   \
    --extra-experimental-features "nix-command flakes"    \
    --option filter-syscalls false                        \
    build                                                 \
 && mkdir /tmp/nix-store-closure                          \
 && cp -R $(nix-store -qR result/) /tmp/nix-store-closure


FROM nixos/nix:latest AS runner
ENV INSIDE_DOCKER="true"
COPY --from=builder /tmp/nix-store-closure /nix/store
COPY . /app
WORKDIR /app
CMD ["./bin/start-prod"]
