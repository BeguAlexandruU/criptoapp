#!/bin/bash

bash db_start.sh 

#bash back_runapp.sh
#bash front_runapp.sh

gnome-terminal --tab --title=back -- bash -c "bash back_runapp.sh ;bash"
# gnome-terminal --tab --title=front -- bash -c "bash front_runapp.sh ;bash"
bash front_runapp.sh