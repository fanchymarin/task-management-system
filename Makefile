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
	@echo -e "  ${GREEN}${BOLD}logs             ${CYAN}- Show the logs of the Django container"
	@echo -e "  ${GREEN}${BOLD}shell            ${CYAN}- Access the Django container shell"
	@echo -e "  ${GREEN}${BOLD}shelldb          ${CYAN}- Access the Postgres container shell"
	@echo -e "  ${GREEN}${BOLD}clean            ${CYAN}- Stop and remove the database volume"
	@echo -e "  ${GREEN}${BOLD}fclean           ${CYAN}- Stop and remove all containers and volumes"
	@echo -e "  ${GREEN}${BOLD}re               ${CYAN}- Clean up all and run the containerized application"
	@echo

up:
	$(call help_message, "Running the containerized application...")
	docker compose --project-name=${PROJECT_NAME} up -d
	$(call help_message, "Application is ready!")

build:
	$(call help_message, "Building the container image...")
	docker compose --project-name=${PROJECT_NAME} build

down:
	$(call help_message, "Stopping the containerized application...")
	docker compose --project-name=${PROJECT_NAME} down

logs:
	$(call help_message, "Showing the logs of the Django container...")
	docker compose --project-name=${PROJECT_NAME} logs -f django || true

shell:
	$(call help_message, "Accessing the Django container shell...")
	docker compose --project-name=${PROJECT_NAME} exec -it django /bin/bash || true

shelldb:
	$(call help_message, "Accessing the Postgres container shell...")
	docker compose --project-name=${PROJECT_NAME} exec -it postgres /bin/bash || true

clean: down
	$(call help_message, "Removing the database volume...")
	docker volume rm -f ${PROJECT_NAME}_postgres-data

fclean: clean
	$(call help_message, "Removing container image...")
	docker rmi -f ${PROJECT_NAME}-django ${PROJECT_NAME}-postgres

re: clean build up

.PHONY: all list up down logs shell shelldb clean fclean re