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


FROM scratch
ENV INSIDE_DOCKER="true"                           \
    PATH="/nix/var/nix/profiles/default/bin:$PATH"
EXPOSE 5000
WORKDIR /app
COPY --from=builder /tmp/nix-store-closure /nix/store
COPY --from=builder /tmp/build/result /app
CMD ["/app/bin/start-prod"]
