FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD P@ssword
ENV MYSQL_DATABASE mydb
ENV MYSQL_USER naresh
ENV MYSQL_PASSWORD P@ssword
COPY initiatedb.sql /docker-entrypoint-initdb.d/
COPY populatedb.sh /docker-entrypoint-initdb.d/