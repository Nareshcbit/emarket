#!/bin/bash
 mysql -h 127.0.0.1 -u$MYSQL_USER -p$MYSQL_PASSWORD mydb< $MYSQL_SCRIPTS_PATH/initiatedb.sql
