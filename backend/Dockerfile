FROM python:3.8-alpine

ENV PYTHONBUFFERED=1

WORKDIR /simtopperBackend

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000