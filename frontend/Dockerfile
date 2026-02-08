# Multi-stage build for optimized image
# Stage 1: Build stage
FROM node:20-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install all dependencies (including dev dependencies for building)
RUN npm ci

# Copy the rest of the application code
COPY . .

# Build the Next.js application for production
RUN npm run build

# Stage 2: Production stage
FROM node:20-alpine AS runner

# Install dumb-init to handle signals properly
RUN apk add --no-cache dumb-init

# Set the working directory
WORKDIR /app

# Copy package.json to get the start script
COPY package*.json ./

# Install only production dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy the built application from the builder stage
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/next.config.mjs ./

# Expose port 3000
EXPOSE 3000

# Define environment variables with defaults
ENV NEXT_PUBLIC_API_URL=http://localhost:8000
ENV NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
ENV NODE_ENV=production

# Create a non-root user for security
RUN addgroup -g 1001 -S nodejs &&\
    adduser -S nextjs -u 1001
USER nextjs

# Start the application with dumb-init
ENTRYPOINT ["dumb-init"]
CMD ["npm", "start"]