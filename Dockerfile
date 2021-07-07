FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install -r r.txt
CMD ["python3", "app.py"]