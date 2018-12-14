#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

echo "Waiting for mysql"
until mysql -h"$host" -P"3306" -u"akita" -p"akitakaito" &> /dev/null
do
  printf "."
  sleep 1
done

echo -e "\nMySQL ready"

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
