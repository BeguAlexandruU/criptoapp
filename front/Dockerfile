# Use the official Bun image as a base
FROM oven/bun:latest

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json bun.lockb ./
RUN bun install

# Copy the rest of the application files
COPY . .

# Build the application
RUN bun run build

# Expose the application port
EXPOSE 4000

# Command to run the application in production mode
CMD ["node", ".output/server/index.mjs"]