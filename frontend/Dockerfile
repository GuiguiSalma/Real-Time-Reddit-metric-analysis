FROM node:14

WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
RUN npm install

# Copy everything else (including src/ and public/)
COPY . /usr/src/app  

CMD ["npm", "start"]
