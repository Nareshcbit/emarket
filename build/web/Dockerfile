FROM python:2.7
RUN apt-get update
COPY . /webapp
RUN apt-get install -y python-pip python-dev default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /webapp/app/requirements.txt
ENV FLASK_ENV="docker"

WORKDIR /webapp/app

EXPOSE 5000

CMD [ "python", "/webapp/app/app.py" ]

