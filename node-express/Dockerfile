FROM node:4.3.0

WORKDIR /home/node
COPY app/app.js app/app.js
COPY app/package.json app/package.json
RUN (cd app; npm install)

CMD ["node","/home/node/app/app.js"]
