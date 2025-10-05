# Use official Node image as base
FROM node:16

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Copy the rest of frontend code
COPY . .

# Expose React dev server port
EXPOSE 3000

# Start React dev server
CMD ["npm", "start"]
