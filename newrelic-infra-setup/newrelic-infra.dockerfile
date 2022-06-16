FROM newrelic/infrastructure:latest
ADD newrelic-infra.yml /etc/newrelic-infra.yml
RUN mkdir /var/log/newrelic-infra && \
    touch /var/log/newrelic-infra/newrelic-infra.log \
    chmod +w /var/log/newrelic-infra/newrelic-infra.log
