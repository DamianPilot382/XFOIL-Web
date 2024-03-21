FROM node:latest

WORKDIR /app

# Copy online package.json and package-lock.json
# The rest of the files will be on the mounted drive from Docker-Compose
COPY ./package*.json /app/.

# Install dependencies
RUN npm install

# Expose ports
EXPOSE 3000 3010

# Start the web server
CMD npm run dev
