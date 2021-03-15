docker-compose build
docker tag microservices_database augustoaccorsi/database-aws
docker tag microservices_engine augustoaccorsi/engine-aws
docker tag postgres augustoaccorsi/postgres-aws
docker tag microservices_nginx augustoaccorsi/nginx-aws
docker push augustoaccorsi/database-aws
docker push augustoaccorsi/postgres-aws
docker push augustoaccorsi/engine-aws
docker push augustoaccorsi/nginx-aws