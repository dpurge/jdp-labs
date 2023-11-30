FROM apache/airflow:2.7.3

ENV AIRFLOW_HOME=/opt/airflow

WORKDIR ${AIRFLOW_HOME}

USER root
RUN apt update -qq && apt install -y \
    python3-pip \
    vim

USER ${AIRFLOW_UID}
