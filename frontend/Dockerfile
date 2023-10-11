 # Use an official Node.js runtime as the base image
FROM node:20 as build-stage

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of your Vue.js application source code to the working directory
COPY . .

# Build your Vue.js application for production
RUN npm run build

# Use an Nginx web server as the base image for the production stage
#FROM nginx:1.25

# Copy the built Vue.js application from the build stage to the Nginx web root directory
#COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80 (the default HTTP port)
#EXPOSE 80

# Start the Nginx web server
#CMD ["nginx", "-g", "daemon off;"]

EXPOSE 8080

CMD ["npm", "run", "serve"]
