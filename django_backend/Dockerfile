FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
	make postgresql-client

ADD . .

EXPOSE 8000

CMD ["make", "up"]