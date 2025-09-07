YELLOW = \033[1;33m
BLUE = \033[1;34m
GREEN = \033[1;32m
CYAN = \033[1;36m
BOLD = \033[1m
RESET = \033[0m

PROJECT_NAME = rest-api

define help_message =
	@echo -e "$(YELLOW)$(BOLD)[Makefile]$(RESET)"
	@echo -e "$(BOLD)${1}$(RESET)"
endef

include .env

all: list

list:
	@echo
	@echo -e "${BLUE}${BOLD}Available recipes:"
	@echo -e "  ${GREEN}${BOLD}list             ${CYAN}- Show this help message"
	@echo -e "  ${GREEN}${BOLD}up               ${CYAN}- Run the containerized application"
	@echo -e "  ${GREEN}${BOLD}build            ${CYAN}- Build the container image"
	@echo -e "  ${GREEN}${BOLD}down             ${CYAN}- Stop the containerized application"
	@echo -e "  ${GREEN}${BOLD}test             ${CYAN}- Run tests in the containerized application"
	@echo -e "  ${GREEN}${BOLD}clean            ${CYAN}- Stop and remove the database volume"
	@echo -e "  ${GREEN}${BOLD}fclean           ${CYAN}- Stop and remove all containers and volumes"
	@echo -e "  ${GREEN}${BOLD}re               ${CYAN}- Clean up all and run the containerized application"
	@echo

up: build
	$(call help_message, "Running the containerized application...")
	docker compose --project-name=${PROJECT_NAME} up -d
	$(call help_message, "Application is ready!")
	$(call help_message, "You can access it at http://localhost:${DJANGO_PORT}/api/")
	@sleep 2
	$(call help_message, "Showing the logs of Django container...")
	docker compose --project-name=${PROJECT_NAME} logs -f django

build:
	$(call help_message, "Building the container image...")
	docker compose --project-name=${PROJECT_NAME} build

down:
	$(call help_message, "Stopping the containerized application...")
	docker compose --project-name=${PROJECT_NAME} down

shell: up
	$(call help_message, "Accessing the Django container shell...")
	docker compose --project-name=${PROJECT_NAME} exec -it django /bin/bash

test: up
	$(call help_message, "Running tests from container...")
	docker compose --project-name=${PROJECT_NAME} exec django make test

clean: down
	$(call help_message, "Removing the database volume...")
	docker volume rm -f ${PROJECT_NAME}_postgres-data

fclean: clean
	$(call help_message, "Removing container image...")
	docker rmi -f ${PROJECT_NAME}-django ${PROJECT_NAME}-postgres

re: fclean up

.PHONY: all list up build down test clean fclean re