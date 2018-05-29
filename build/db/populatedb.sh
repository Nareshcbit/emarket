#!/bin/bash
 mysql -h 127.0.0.1 -u$MYSQL_USER -pMYSQL_PASSWORD mydb< $MYSQL_SCRIPTS_PATH/initiatedb.sql
