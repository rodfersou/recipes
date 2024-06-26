FROM recipes-api-deps AS deps

FROM nixos/nix:latest AS runner
ENV INSIDE_DOCKER="true"
COPY --from=deps /tmp/nix-store-closure /nix/store
COPY . /app
WORKDIR /app
CMD ["./scripts/start-prod"]
