FROM python:3.5.6-jessie

ADD requirements.txt .
RUN pip install -r requirements.txt