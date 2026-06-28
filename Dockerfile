######### STAGE 1 - Generate html election maps #########
FROM python:3.14.3-slim-trixie AS python-stage

WORKDIR /app

## Copy all Python scripts
COPY requirements.txt ./ \
    mapGenerators ./

RUN python3 -m pip install --upgrade pip \
    && python3 -m \
    pip install -r requirements.txt

### Create pages/main/parliament_charts directory
RUN mkdir -p pages/main/parliament_charts

### Create pages/elections directory
RUN mkdir -p pages/elections

## Run all python scripts to generate the maps
RUN python generateCanadianElectionFiles.py


######### STAGE 2 - Minify elections_style.css #########
FROM node:lts-alpine AS minify-stage

WORKDIR /app

# Install CSS minifier (e.g., csso-cli)
RUN npm install -g csso-cli

# Copy elections_style.css to /app/stylesheets
COPY ./pages/main/elections_style.css ./stylesheets/elections_style.css

# Minify elections_style.css
RUN csso ./stylesheets/elections_style.css --output ./elections_style.css


######### STAGE 3 - Copy html election maps and minifed CSS to final container #########
FROM nginxinc/nginx-unprivileged:alpine3.23-perl

## Copy sitemap.xml to nginx/html
COPY ./pages/sitemap.xml /usr/share/nginx/html/pages/sitemap.xml

## Copy main folder to nginx/html 
COPY ./pages/main /usr/share/nginx/html/pages/main

## Set canadianelections.net to automatically redirect to "/pages/main/elections.html", no explicit path required
COPY default.conf /etc/nginx/conf.d/default.conf

## Allow permissions to access favicon
USER root
RUN chmod -R 755 /usr/share/nginx/html/pages/main/favicon

## Copy elections_style.css from minify-stage
COPY --from=minify-stage /app/elections_style.css /usr/share/nginx/html/pages/main/elections_style.css

## Copy the election pages to the nginx/html/pages/elections folder
COPY --from=python-stage /app/pages/elections /usr/share/nginx/html/pages/elections

## Copy the parliament_charts to the nginx/html/pages/main/parliament_charts folder
COPY --from=python-stage /app/pages/main/parliament_charts /usr/share/nginx/html/pages/main/parliament_charts

USER nginx
EXPOSE 8080
