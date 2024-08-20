#!/bin/bash

PATH_DB="../back/database/"

PATH_ORIGIN=$(pwd)

#connect to virtual environment


#start docker
sudo systemctl start docker

cd $PATH_DB
docker compose up -d