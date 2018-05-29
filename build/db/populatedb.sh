#!/bin/bash
 mysql -u$MYSQL_USER -p$MYSQL_PASSWORD mydb< $MYSQL_SCRIPTS_PATH/initiatedb.sql
