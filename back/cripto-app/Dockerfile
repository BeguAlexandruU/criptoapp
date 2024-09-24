FROM python:3.12.4-alpine

EXPOSE 5001

WORKDIR /code

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN apk add mysql-client
RUN pip install poetry
RUN apk add --no-cache bash
COPY  . /code

COPY docker/cripto_app.sh /code/docker/
RUN chmod +x /code/docker/cripto_app.sh

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi && pip install nowpayment