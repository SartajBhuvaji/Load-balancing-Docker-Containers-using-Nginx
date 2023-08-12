FROM python:3.8-alpine

# switch working directory
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app