#!/bin/bash

apt-get install zlib1g-dev && \
cd /opt && \
wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz && \
tar -xvf Python-3.6.9.tgz && \
cd Python-3.6.9/ && \
./configure && \
make && \
make install && \
rm -R /opt/Python-3.6.9.tgz
