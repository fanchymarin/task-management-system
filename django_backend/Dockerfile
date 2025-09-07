FROM python:3.10

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
	make postgresql-client

# Add source code
ADD . .

# Install Python dependencies
RUN pip install --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt

# Give execution permissions to the entrypoint script
RUN chmod +x ./scripts/entrypoint.sh

EXPOSE 8000

CMD ["/bin/bash", "./scripts/entrypoint.sh"]