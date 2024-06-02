FROM grafana/grafana-enterprise

USER root
RUN mkdir -p /workspace
RUN apk add --update --no-cache nodejs npm go-task
RUN apk add --update --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ go-jsonnet 

# COPY ./plugins/dpurge-lab1-panel/dist /var/lib/grafana/plugins/dpurge-lab-panel
# COPY ./plugins/dpurge-lab1-app/dist /var/lib/grafana/plugins/dpurge-lab-app
# COPY ./provisioning/ /etc/grafana/provisioning/
