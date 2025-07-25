### STAGE 1
FROM python:3.13.5-slim-bullseye as python-stage

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgdal-dev \
    python3-dev \
    build-essential \
    gcc \
    clang

## Copy requirements.txt
COPY requirements.txt ./ \
    CanadianElection1867.py ./ \
    CanadianElection2019.py ./ \
    CanadianElection2021.py ./

## Install all requirements
RUN python3 -m pip install --upgrade pip \
    && python3 -m \
    pip install -r requirements.txt

## Copy voting_data and shapefiles
COPY voting_data ./voting_data \
    districts2 ./districts2

## Run all python scripts to generate the maps
CMD ["python3", "./CanadianElection1867.py", "./CanadianElection2019.py; ./CanadianElection2021.py"]


### STAGE 2
FROM nginxinc/nginx-unprivileged:stable-alpine

## Copy main folder to nginx/html 
COPY ./pages/main /usr/share/nginx/html/pages/main

## Make elections folder in /usr/share/nginx/html
# USER root
# RUN mkdir -p /usr/share/nginx/pages/elections

## Copy the maps to the nginx/html/pages/elections folder
COPY --from=python-stage /app/pages/elections/election1867.html /usr/share/nginx/html/pages/elections/election1867.html
COPY --from=python-stage /app/pages/elections/election2019.html /usr/share/nginx/html/pages/elections/election2019.html
COPY --from=python-stage /app/pages/elections/election2021.html /usr/share/nginx/html/pages/elections/election2021.html

USER nginx
EXPOSE 8080
