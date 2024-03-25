# pull official base image
FROM python:3.9.5-slim-buster@sha256:f42d92068b29045b6893da82032ca4fcf96193be5dcbdcfcba948489efa9e832 as base

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

########
# Test #
########
FROM base
COPY . /usr/src/app/
RUN pytest project/tests


#######
# Dev #
#######
FROM base 