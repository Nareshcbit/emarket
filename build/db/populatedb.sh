#!/bin/bash
 mysql -u$MYSQL_USER -pMYSQL_PASSWORD mydb< $MYSQL_SCRIPTS_PATH/initiatedb.sql
