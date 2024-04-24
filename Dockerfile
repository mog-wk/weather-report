# syntax=docker/dockerfile:1
FROM python:3-alpine
WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ["python", "main.py"]
