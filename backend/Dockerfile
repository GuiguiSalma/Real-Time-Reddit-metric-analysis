FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9092 7077

CMD ["python", "./main.py"]
