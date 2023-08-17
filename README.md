# Tasks.cx

This project defines the proposal of Task Exchange protocol, an open standard data format for representing, exchanging tasks, projects over the network.

## Concepts and Architecture

[Concepts](./docs/index.md)

## Installation steps

### Environment variables

Create the .env file and change the keys according to your setup

```sh
API_VERSION="1"
DEBUG=1
MODE="dev"

MONGO_INITDB_ROOT_DATABASE="taskcx"
MONGO_INITDB_ROOT_HOST="localhost"
MONGO_INITDB_ROOT_PORT=27017
MONGO_INITDB_ROOT_USERNAME="root"
MONGO_INITDB_ROOT_PASSWORD="simplepassword"

MAILGUN_DOMAIN="email.tasks.cx"
MAILGUN_DEFAULT_USER="notification"
MAILGUN_KEY="key-YOUR-MAILGUN-KEY"
```

We currently use Mailgun for email delivery, please follow [this](https://documentation.mailgun.com/en/latest/index.html) instruction to get your API key.

### Start services

Our current setup offers out of the box docker setup.
Simply run the docker compose command to start everything

```
docker compose up
```

You can also choose to run services individually

#### Setup and run MongoDB

Follow the official [MongoDB installation](https://www.mongodb.com/docs/manual/installation/) guide

Remember to update the credentials in .env

#### Run API service

1. Create python virtual env
2. Run `server.py`

```
python src/server.py
```

#### Run background worker

We use Celery for running and managing background jobs. Here is the default comamnd to start a celery worker

```
celery --workdir src -A jobs worker --loglevel INFO
```

## License

[License](./LICENSE)