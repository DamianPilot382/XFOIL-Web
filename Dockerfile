FROM node:latest

WORKDIR /app

COPY ./package*.json /app/.

RUN npm install

EXPOSE 3000 3010

CMD npm run dev
