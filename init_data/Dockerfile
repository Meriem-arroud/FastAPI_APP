FROM postgres as postgres_base
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres

WORKDIR /init

COPY ./init_data /init/init_data

