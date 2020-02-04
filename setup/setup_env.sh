#!/bin/bash

mkdir -p /usr/local/hadoop && \
	rm /etc/environment && \
	touch /etc/environment && \
	echo 'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"' >> /etc/environment && \
	echo 'JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/"' >> /etc/environment && \
	source /etc/environment
