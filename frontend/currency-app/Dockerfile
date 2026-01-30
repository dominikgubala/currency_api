# Build Angular app
FROM node:20 AS build
WORKDIR /app
COPY . ./
RUN npm install && npm run build

# Run with NGINX
FROM nginx:alpine
COPY --from=build /app/dist/currency-app/browser /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
