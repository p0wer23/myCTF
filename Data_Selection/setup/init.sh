#!/bin/sh
service mariadb start && service apache2 start
USER="Cybercon"
PASSWORD="G4m30f1if3"

echo "Creating new user ${MYSQL_USER} ..."
mysql -uroot -e "CREATE USER '${USER}'@'localhost' IDENTIFIED BY '${PASSWORD}';"
echo "Granting privileges..."
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO '${USER}'@'localhost';"
mysql -uroot -e "GRANT FILE ON *.* TO '${USER}'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
echo "Done! Permissions granted"
mysql -u$USER -p$PASSWORD -e "CREATE database Cybercon;"
mysql -u$USER -p$PASSWORD Cybercon  < /init.db
echo "All done."
sleep 5
python3 -u /app.py