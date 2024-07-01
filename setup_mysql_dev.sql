CREATE DATABASE IF NOT EXISTS mentconnect_db;
CREATE USER IF NOT EXISTS 'mentconnect_dev'@'localhost';
GRANT ALL PRIVILEGES ON mentconnect_db.* TO 'mentconnect_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'mentconnect_dev'@'localhost';
FLUSH PRIVILEGES;
