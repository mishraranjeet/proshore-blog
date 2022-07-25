FROM python:3.10-slim-buster

ENV PYTHONBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app

RUN chmod 777 ./run.sh
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic

ENV env $env

CMD ["./run.sh"]


EXPOSE 8000