#!/bin/bash
 mysql -h 192.168.0.13 -unaresh -pP@ssword < /docker-entrypoint-initdb.d/initiatedb.sql
