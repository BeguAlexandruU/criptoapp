#!/bin/bash

PATH_DB="../back/database/"

PATH_ORIGIN=$(pwd)

#connect to virtual environment
source ../back/env/bin/activate

#start docker
sudo systemctl start docker

cd $PATH_DB
docker-compose up


deactivate