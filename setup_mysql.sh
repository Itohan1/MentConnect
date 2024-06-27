#!/bin/bash

# Create database if not exists
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DATABASE;"

# Create user and grant privileges
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "CREATE USER IF NOT EXISTS '$USER'@'localhost' IDENTIFIED BY '$PASSWORD';"
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "GRANT ALL PRIVILEGES ON $DATABASE.* TO '$USER'@'localhost';"
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "GRANT SELECT ON performance_schema.* TO '$USER'@'localhost';"

# Flush privileges
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "FLUSH PRIVILEGES;"

echo "MySQL server setup complete."

