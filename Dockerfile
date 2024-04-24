# syntax=docker/dockerfile:1
FROM python:3.12.3-alpine:3.19
WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./src/report.py"]

RUN ["python", "src/main.py"]
