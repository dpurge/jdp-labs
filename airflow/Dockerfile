FROM apache/airflow:2.7.3

ENV AIRFLOW_HOME=/opt/airflow

WORKDIR ${AIRFLOW_HOME}

USER root
RUN apt update -qq && apt install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    gpg \
    jq \
    libpq-dev \
    openssh-client \
    tzdata \
    unzip \
    wget \
    zip

USER ${AIRFLOW_UID}
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /tmp/requirements.txt
