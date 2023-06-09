FROM postgres:14.8-bullseye

ARG user=postgres

COPY --chown=$user:$user init_postgres.sh /docker-entrypoint-initdb.d/
RUN chmod a+x /docker-entrypoint-initdb.d/init_postgres.sh

USER $user
