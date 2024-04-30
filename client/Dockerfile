# client/Dockerfile

# Stage 1: Build React App
FROM node:14 AS builder

WORKDIR /app

COPY .//package.json ./package-lock.json ./

RUN npm install

COPY ./src ./src

COPY ./public ./public

RUN npm run build

# Stage 2: Serve the application with Nginx
FROM nginx:stable-alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
