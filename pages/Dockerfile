### STILL TESTING

FROM python:3.12.8-alpine3.21

## Copy requirements.txt
ADD requirements.txt ./ && \
    CanadianElection2019.py ./ && \
    CanadianElection2021.py ./


## Install all requirements
RUN python3 -m pip install --upgrade pip \
    && python3 -m \
    pip install -r requirements.txt

### CMD ["python", "./CanadianElection2019.py; ./CanadianElection2021.py"]

COPY election2019.html /usr/share/nginx/html/election2019.html && \
     election2021.html /usr/share/nginx/html/election2021.html
