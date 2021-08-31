FROM python:3.7-alpine
MAINTAINER JvitorS23

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
RUN apk update && apk add bash

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN chmod 755 /app/entrypoint.sh
