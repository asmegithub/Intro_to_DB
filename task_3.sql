#!/bin/bash

-- # Check if the database name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide the database name as an argument."
    exit 1
fi

-- # Store the database name in a variable
database=$1

-- # Execute the MySQL command to list all tables in the specified database
mysql -e "USE $database; SHOW TABLES;"