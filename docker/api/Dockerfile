FROM python:3.10.12-slim-buster

ARG user=admin

WORKDIR /app

# install system packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install --no-install-recommends -y -q \
            curl \
            netcat &&\
    # add new user with sudo privileges
    useradd --no-create-home --user-group -s /bin/bash $user &&\
    # cleanup
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

COPY --chown=$user:$user pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir -U pip setuptools wheel poetry &&\
    poetry config virtualenvs.create false &&\
    poetry install --no-cache --no-interaction --no-ansi --no-root

COPY --chown=$user:$user . .

USER $user

ENTRYPOINT ["/bin/bash", "/app/docker/api/init_app.sh"]
