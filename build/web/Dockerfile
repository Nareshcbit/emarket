FROM python:2.7

RUN apt-get update && apt-get install -y python-pip python-dev default-libmysqlclient-dev

COPY . /webapp
RUN pip install --upgrade pip && pip install --no-cache-dir -r /webapp/app/requirements.txt



ENV FLASK_ENV="docker"
ENV DB_NAME mydb
ENV DB_USER naresh
ENV DB_USER_PASSWORD P@ssword
ENV DB_HOST 192.168.0.2

RUN echo "" >> /webapp/app/dbconf.yaml && \
    echo "DB_HOST:" "'"${DB_HOST}"'" >> /webapp/app/dbconf.yaml && \
    echo "DB_NAME:" "'"${DB_NAME}"'" >> /webapp/app/dbconf.yaml && \
    echo "DB_USER:" "'"${DB_USER}"'" >> /webapp/app/dbconf.yaml && \
    echo "DB_USER_PASSWORD:" "'"${DB_USER_PASSWORD}"'" >> /webapp/app/dbconf.yaml



WORKDIR /webapp/app

EXPOSE 5000

CMD [ "python", "/webapp/app/app.py" ]

