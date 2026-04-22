FROM python:3.15.0a8-trixie

WORKDIR /app

RUN apt-get update

## COPY FastAPI APP TO THE CONTAINER
COPY app ./

## INSTALL REQUIREMENTS
RUN python3 -m pip install --upgrade pip \
    && python3 -m \
    pip install -r requirements.txt

## ADD NON-ROOT USER
RUN groupadd --gid 1000 fastapi \
    && useradd --uid 1000 --gid 1000 -m fastapi \
    && chown -R fastapi:fastapi /app

## SWITCH TO fastapi USER
USER fastapi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]