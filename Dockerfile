FROM node:latest

WORKDIR /app
#COPY WebApp/package.json /app
COPY WebApp /app
RUN npm install
EXPOSE 8083
CMD node index.js
