
FROM python:3.8-alpine
MAINTAINER Ankit Sharma Docker Ltd

ENV PYTHONUNBUFFERED 1

ARG REQ_FILE
COPY $REQ_FILE /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /django_project
WORKDIR /django_project
COPY ./django_project /django_project

RUN adduser -D user
USER user