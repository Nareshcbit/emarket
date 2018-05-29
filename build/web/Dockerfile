FROM python:2.7

RUN apt-get update && apt-get install -y python-pip python-dev default-libmysqlclient-dev

COPY . /webapp
RUN pip install --upgrade pip && pip install --no-cache-dir -r /webapp/app/requirements.txt



ENV FLASK_ENV="docker"
ENV MYSQL_DATABASE mydb
ENV MYSQL_USER naresh
ENV MYSQL_PASSWORD P@ssword
ENV MYSQL_HOST 192.168.0.13

RUN echo "MYSQL_HOST_N:" "'"${MYSQL_HOST}"'" >> /webapp/app/dbconf.yaml && \
    echo "MYSQL_DATABASE_N:" "'"${MYSQL_DATABASE}"'" >> /webapp/app/dbconf.yaml && \
    echo "MYSQL_USER_N:" "'"${MYSQL_USER}"'" >> /webapp/app/dbconf.yaml && \
    echo "MYSQL_PASSWORD_N:" "'"${MYSQL_PASSWORD}"'" >> /webapp/app/dbconf.yaml



WORKDIR /webapp/app

EXPOSE 5000

CMD [ "python", "/webapp/app/app.py" ]

