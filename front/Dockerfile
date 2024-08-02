# Description: Fișierul de configurare pentru construirea imaginii Docker a aplicației front-end.
FROM oven/bun:latest as build

WORKDIR /app

COPY package.json bun.lockb ./

RUN bun install

COPY . .

# Production build
RUN bun run build

FROM oven/bun:latest as run

WORKDIR /app

COPY --from=build /app/.output /app/.output
COPY --from=build /app/node_modules /app/node_modules
COPY --from=build /app/.nuxt /app/.nuxt
COPY --from=build /app/nuxt.config.ts /app/nuxt.config.ts
COPY --from=build /app/package.json /app/package.json

EXPOSE 3000

CMD ["bun", "run", "start"]
