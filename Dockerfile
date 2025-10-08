### STAGE 1 - Generate html election maps
FROM python:3.13.5-slim-bullseye as python-stage

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgdal-dev \
    python3-dev \
    build-essential \
    gcc \
    clang

## Copy requirements.txt and all Python scripts
COPY requirements.txt ./ \
    mapGenerators ./

## Install all requirements
RUN python3 -m pip install --upgrade pip \
    && python3 -m \
    pip install -r requirements.txt

## Copy voting_data to the container
COPY voting_data ./voting_data

# Unzip districts2 and copy it to the container
ADD districts2.tar.gz ./

## Run all python scripts to generate the maps
RUN python CanadianElection1867.py && python CanadianElection1872.py \
    && python CanadianElection1874.py && python CanadianElection1878.py \
    && python CanadianElection1882.py && python CanadianElection1887.py \
    && python CanadianElection1891.py && python CanadianElection1896.py \
    && python CanadianElection1900.py && python CanadianElection1904.py \
    && python CanadianElection2019.py && python CanadianElection2021.py


### STAGE 2 - Minify elections_style.css
FROM node:lts-alpine as minify-stage

WORKDIR /app

# Install CSS minifier (e.g., csso-cli)
RUN npm install -g csso-cli

# Copy elections_style.css to /app/stylesheets
COPY ./pages/main/elections_style.css ./stylesheets/elections_style.css

# Minify elections_style.css
RUN csso ./stylesheets/elections_style.css --output ./elections_style.css


### STAGE 3 - Copy html election maps and minifed CSS to final container
FROM nginxinc/nginx-unprivileged:stable-alpine

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

## Copy the maps to the nginx/html/pages/elections folder
COPY --from=python-stage /app/pages/elections/election1867.html /usr/share/nginx/html/pages/elections/election1867.html
COPY --from=python-stage /app/pages/elections/election1872.html /usr/share/nginx/html/pages/elections/election1872.html
COPY --from=python-stage /app/pages/elections/election1874.html /usr/share/nginx/html/pages/elections/election1874.html
COPY --from=python-stage /app/pages/elections/election1878.html /usr/share/nginx/html/pages/elections/election1878.html
COPY --from=python-stage /app/pages/elections/election1882.html /usr/share/nginx/html/pages/elections/election1882.html
COPY --from=python-stage /app/pages/elections/election1887.html /usr/share/nginx/html/pages/elections/election1887.html
COPY --from=python-stage /app/pages/elections/election1891.html /usr/share/nginx/html/pages/elections/election1891.html
COPY --from=python-stage /app/pages/elections/election1896.html /usr/share/nginx/html/pages/elections/election1896.html
COPY --from=python-stage /app/pages/elections/election1900.html /usr/share/nginx/html/pages/elections/election1900.html
COPY --from=python-stage /app/pages/elections/election1904.html /usr/share/nginx/html/pages/elections/election1904.html
COPY --from=python-stage /app/pages/elections/election2019.html /usr/share/nginx/html/pages/elections/election2019.html
COPY --from=python-stage /app/pages/elections/election2021.html /usr/share/nginx/html/pages/elections/election2021.html

## Copy the parliament_charts to the nginx/html/pages/main/parliament_charts folder
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1867.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1867.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1872.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1872.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1874.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1874.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1878.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1878.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1882.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1882.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1887.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1887.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1891.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1891.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1896.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1896.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1900.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1900.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart1904.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart1904.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart2019.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart2019.html
COPY --from=python-stage /app/pages/main/parliament_charts/parl_chart2021.html /usr/share/nginx/html/pages/main/parliament_charts/parl_chart2021.html

USER nginx
EXPOSE 8080
