# client/Dockerfile

# Stage 1: Build React App
FROM node:14 AS builder

WORKDIR /app

COPY ./package.json ./package-lock.json ./

RUN npm install

COPY ./src ./src

COPY ./public ./public

RUN npm run build