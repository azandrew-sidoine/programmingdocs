FROM node:12-alpine

RUN apk add --no-cache python2 g++ make

WORKDIR /home

COPY app/ .

RUN yarn install --production

CMD [ "npm",  "start"]

EXPOSE 3000