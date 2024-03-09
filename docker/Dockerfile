FROM python:3.11.6-slim-bullseye

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  apt-utils \
  gcc \
  zsh \
  git \
  build-essential && \
  apt-get autoremove -y && \
  apt-get clean -y && \ 
  rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install --upgrade pip setuptools

WORKDIR /code
COPY requirements.txt /code/
RUN pip --no-cache-dir install -r requirements.txt