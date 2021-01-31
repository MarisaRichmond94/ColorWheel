FROM python:3.8.2-slim as base

FROM base as builder
SHELL ["/bin/bash", "-c"]
RUN pip install pipenv
RUN apt-get update \
  && apt-get install -y build-essential git \
  && apt-get clean
COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock
ENV PIPENV_VENV_IN_PROJECT=true
RUN pipenv lock
RUN pipenv install --system --deploy --ignore-pipfile

FROM base
ENV ENVIRONMENT=docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/code
RUN apt-get update && apt-get install -y gettext-base && apt-get clean
COPY --from=builder /usr/local /usr/local
WORKDIR /code/api
COPY . .
CMD alembic -c chalicelib/alembic.ini upgrade head \
  && chalice local --host 0.0.0.0 --stage docker --no-autoreload
