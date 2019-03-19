FROM node:4.3.0

WORKDIR /home/node
COPY app/app.js app/app.js
COPY app/package.json app/package.json
RUN (cd app; npm install)

# The first step gets all the modules

FROM nablact/nabla-node-base:v0.3
COPY --from=0 /home/node/app/ /home/node/app/
CMD ["/home/node/app/app.js"]
