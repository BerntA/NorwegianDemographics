#!/bin/bash

host="127.0.0.1 localhost
192.168.22.29 master
192.168.22.162 slave-1
192.168.22.97 slave-2
192.168.22.196 slave-3

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts"
rm /etc/hosts && touch /etc/hosts && echo "$host" >> /etc/hosts

mkdir -p /usr/local/hadoop && \
	rm /etc/environment && \
	touch /etc/environment && \
	echo 'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/hadoop/bin:/usr/local/hadoop/sbin:/usr/local/spark/bin:/usr/local/spark/sbin"' >> /etc/environment && \
	echo 'JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"' >> /etc/environment && \
	echo 'SPARK_HOME="/usr/local/spark"' >> /etc/environment && \
	echo 'HADOOP_CONF_DIR="/usr/local/hadoop/etc/hadoop"' >> /etc/environment && \
	echo 'YARN_CONF_DIR="/usr/local/hadoop/etc/hadoop"' >> /etc/environment && \
	source /etc/environment && \
	sudo chown -R ubuntu /usr/local/hadoop && \
	sudo chown -R ubuntu /usr/local/spark
