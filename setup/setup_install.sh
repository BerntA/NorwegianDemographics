#!/bin/bash

apt-get install default-jdk && apt-get update && apt-get install -y build-essential python && apt-get install python-pip && pip3 install mrjob==0.5.10 && pip3 install pyspark==2.4.5 && \
wget archive.apache.org/dist/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz && \
tar -xzvf hadoop-3.1.1.tar.gz && \
mv hadoop-3.1.1/* /usr/local/hadoop && \
rm hadoop-3.1.1.tar.gz && \
rm -rf hadoop-3.1.1
