docker-compose build
docker tag database 571785655335.dkr.ecr.sa-east-1.amazonaws.com/database
docker tag engine 571785655335.dkr.ecr.sa-east-1.amazonaws.com/engine
docker tag postgres 571785655335.dkr.ecr.sa-east-1.amazonaws.com/postgres
docker tag nginx 571785655335.dkr.ecr.sa-east-1.amazonaws.com/nginx
docker push 571785655335.dkr.ecr.sa-east-1.amazonaws.com/database
docker push 571785655335.dkr.ecr.sa-east-1.amazonaws.com/engine
docker push 571785655335.dkr.ecr.sa-east-1.amazonaws.com/nginx
docker push 571785655335.dkr.ecr.sa-east-1.amazonaws.com/postgres