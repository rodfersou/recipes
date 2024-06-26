FROM ghcr.io/rodfersou/recipes-api-deps:latest AS runner
ENV INSIDE_DOCKER="true"
COPY . /app
WORKDIR /app
CMD ["./scripts/start-prod"]
