FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get install -y build-essential wget curl apt-transport-https mysql-client

RUN mkdir -p /app
WORKDIR /app

ADD Pipfile /app
ADD Pipfile.lock /app

RUN pip install pipenv
RUN pipenv install --system

ADD . /app
