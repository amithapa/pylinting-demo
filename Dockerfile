FROM python:3.9-alpine

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/

WORKDIR /src
