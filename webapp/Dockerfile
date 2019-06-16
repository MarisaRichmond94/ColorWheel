FROM node:8.10-stretch
WORKDIR /client
COPY package*.json ./
RUN npm install && npm cache clean --force
COPY . $WORKDIR
EXPOSE 3000
ENV NAME colorwheel_client
CMD ["npm", "run", "start"]