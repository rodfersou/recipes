FROM ghcr.io/rodfersou/recipes-api-deps:latest AS runner
COPY . /app
WORKDIR /app
CMD ["./scripts/start-prod"]
