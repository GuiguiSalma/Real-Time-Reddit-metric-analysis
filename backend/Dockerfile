FROM python:3.8-slim-buster

WORKDIR /usr/src/app


COPY . /usr/src/app


RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "app/main.py"]
