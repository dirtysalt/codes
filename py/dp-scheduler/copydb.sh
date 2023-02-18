#!/usr/bin/env bash
#Copyright (C) dirlt

###TO BE CHANGE
if [ $# != 2 ]
then
    echo "usage:import <source-db> <dest-db>"
    exit 1
else
    FROM=$1
    TO=$2
    sqlite3 $FROM '.dump jobTable' > /tmp/nsched-swap.sql
    sqlite3 $TO '.read /tmp/nsched-swap.sql' 2>/dev/null 

    #out 
    # mysqldump -h localhost -u root -p bright >/tmp/bright.dump.sql
    # mysqldump -h localhost -u root -p bright table >/tmp/bright.dump.sql

    #in
    #mysql-uroot -p -D test<c:/temp/db_test.backup;
fi

