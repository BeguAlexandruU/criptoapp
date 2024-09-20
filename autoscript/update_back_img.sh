#!/bin/bash

PATH_G="../back/cripto-app/"

cd $PATH_G

sudo docker rmi cripto_app_back:v01 .

sudo docker build -t cripto_app_back:v01 .
