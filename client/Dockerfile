# client/Dockerfile

# Stage 1: Build React App
FROM node:14 AS builder

WORKDIR /app

COPY ./package*.json ./

RUN npm install

COPY . .

RUN npm run build