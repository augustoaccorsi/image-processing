docker-compose build
docker tag database augustoaccorsi/database-aws
docker tag engine augustoaccorsi/engine-aws
docker tag postgres augustoaccorsi/postgres-aws
docker tag nginx augustoaccorsi/nginx-aws
docker push augustoaccorsi/database-aws
docker push augustoaccorsi/postgres-aws
docker push augustoaccorsi/engine-aws
docker push augustoaccorsi/nginx-aws