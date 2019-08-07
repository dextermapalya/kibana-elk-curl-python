#passed in from docker-compose.yml this is set as args: - ELK_VERSION=${ELK_VERSION}  
ARG ELK_VERSION 
FROM docker.elastic.co/logstash/logstash:$ELK_VERSION

RUN rm -f /usr/share/logstash/pipeline/logstash.conf
COPY pipeline /usr/share/logstash/pipeline/
