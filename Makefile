# Description: Makefile for the project cripto app

# Cripo app commands for docker compose
run:
	@echo "Running the application"
	@docker compose up -d

down:
	@echo "Stopping the application"
	@docker compose down

# Rerun the application
rrun: down run


# Front image commands
build_front_image:
	@echo "Building the front image"
	@docker build -t cripto-app:v1 -f ./front/Dockerfile ./front

remove_front_image:
	@echo "Removing the front image"
	@docker rmi cripto-app:v1

rebuid_front_image: remove_front_image build_front_image

