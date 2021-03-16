docker tag microservices_engine:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:engine
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:engine

docker tag microservices_database:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:database
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:database

docker tag microservices_nginx:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:nginx
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:nginx

docker tag postgres:latest 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:postgres
docker push 571785655335.dkr.ecr.us-east-1.amazonaws.com/augusto-accorsi-tcc:postgres