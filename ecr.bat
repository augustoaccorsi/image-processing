docker tag microservices_nginx:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/nginx:latest
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/nginx:latest

docker tag postgres:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/database-db:latest
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/database-db:latest

docker tag microservices_database:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/database:latest
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/database:latest

docker tag microservices_engine:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/engine:latest
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc/engine:latest