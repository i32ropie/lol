#!/bin/sh
docker exec -i lol_database_1 sh -c "apk add mongodb-tools && mongoimport -c users -d lol_bot --drop" < database.jsonb