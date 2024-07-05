# ReactApp Dockerfile

FROM node:14

WORKDIR /app

COPY ./package*.json ./

# VOLUME ["/app"]

RUN npm install

COPY . .

EXPOSE 80 3000

# RUN npm run build

# RUN npm install -g serve

# CMD ["serve", "-s", "build", "-l", "3000"]

CMD ["npm", "start"]