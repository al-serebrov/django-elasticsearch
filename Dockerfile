FROM python:3-jessie

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
# ENV DJANGO_SETTINGS_MODULE=code.esdjango.settings
