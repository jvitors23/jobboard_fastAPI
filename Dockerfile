FROM python:3.8
MAINTAINER JvitorS23

ENV PYTHONUNBUFFERED=1

RUN apt-get update --yes --quiet && \
	apt-get upgrade -y && \
	apt-get install --yes --quiet --no-install-recommends \
		build-essential \
		libpq-dev \
		libmariadbclient-dev \
		libjpeg62-turbo-dev \
		zlib1g-dev \
		libwebp-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

