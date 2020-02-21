#!/bin/bash

mkdir -p /usr/local/spark && \ 
wget https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz && \ 
tar -xzf spark-2.4.5-bin-hadoop2.7.tgz && mv spark-2.4.5-bin-hadoop2.7 /usr/local/spark 
