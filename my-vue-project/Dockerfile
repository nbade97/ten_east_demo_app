# Stage 1: Build the Vue.js application
FROM node:14 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json /app/

# Install the dependencies
RUN npm install

# Copy the rest of the application code
COPY . /app/

# Build the Vue.js application
RUN npm run build

# Stage 2: Serve the application using a lightweight web server
FROM nginx:alpine

# Copy the built files from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose the necessary port
EXPOSE 80

# Define the command to run the web server
CMD ["nginx", "-g", "daemon off;"]
