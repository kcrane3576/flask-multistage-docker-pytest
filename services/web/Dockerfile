# pull official base image
FROM python:3.9.5-slim-buster as base

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
# COPY ./requirements.txt /usr/src/app/requirements.txt
# TODO this should not need to be done like this
COPY /services/web/ /usr/src/app/

# COPY . /usr/src/app/

RUN ls -la
# RUN pip install -r requirements.txt
RUN pip install -r requirements.txt
RUN ls -la

FROM base
# RUN cd project/tests/unit
RUN ls -la
# RUN pytest project/tests/unit/test_app.py
ARG cache=1
RUN pytest project/tests

FROM base 
CMD python

RUN ls -la


# copy project
# COPY . /usr/src/app/