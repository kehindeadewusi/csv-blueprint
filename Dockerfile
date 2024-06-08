# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONUNBUFFERED=1
ENV FORCE_COLOR=1

WORKDIR /app

ADD . /app
RUN pip install .

# RUN useradd --create-home --shell /bin/bash app_user
# USER app_user
