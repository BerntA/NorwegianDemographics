#!/bin/bash

cd ./
apt-get install default-jdk && apt-get update && apt-get install -y build-essential python && \
wget archive.apache.org/dist/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz && \
tar -xzvf hadoop-3.1.1.tar.gz && \
mv hadoop-3.1.1/* /usr/local/hadoop && \
rm hadoop-3.1.1.tar.gz && \
rm -r hadoop-3.1.1

