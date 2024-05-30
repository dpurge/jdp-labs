FROM jenkins/jenkins:lts

USER root
ADD https://download.docker.com/linux/static/stable/x86_64/docker-26.0.0.tgz /opt/
RUN ln -s /opt/docker/docker /usr/local/bin/docker

USER jenkins
