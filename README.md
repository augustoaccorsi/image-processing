[![Build Status](https://travis-ci.com/augustoaccorsi/microservices.svg?branch=main)](https://travis-ci.com/augustoaccorsi/microservices)

# Image Processing Microservice
This project aims to be a simple image processing microservice for academic purpose.

## Idea
The idea came up from the objective to create a microservice that has a huge CPU consumption, so would be easier to work with its scalability.

## How to run locally
  1. Install [Docker Desktop](https://docs.docker.com/get-docker/)
  2. Run the command ```docker-compose up --build``` to build the Docker images
  3. Run the Docker Container
  4. The service will be available on ```localholst:80```

## How to run on EB locally
  1. Install [EB cli](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html) with command ```pip install awsebcli --upgrade --user```
  2. Run the command ```eb local run```, the image will be available on Docker
  3. Run the Docker Container
  4. The service will be available on ```localholst:80```

## How to use
TBD

## Microservice Architecture
TBD