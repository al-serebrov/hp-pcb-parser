FROM python:3.5.6-jessie

RUN mkdir /code
WORKDIR /code
ADD . .

RUN pip install -r requirements.txt

EXPOSE $PORT
EXPOSE 8080

CMD python app.py


