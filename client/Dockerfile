# Stage 1: Build the React application
FROM node:14 as builder

# Set the working directory in the builder stage
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:stable-alpine

# Copy the built app from the builder stage
COPY --from=builder /usr/src/app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx and serve the application
CMD ["nginx", "-g", "daemon off;"]
