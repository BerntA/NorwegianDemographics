#!/bin/sh

cd ./

rm -rf /etc/environment
touch /etc/environment
echo 'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"' > /etc/environment
#echo 'JAVA_HOME="/usr/lib/jvm/java-8-oracle/jre"' > /etc/environment << update this to the correct path
source /etc/environment

apt-get install default-jdk && apt-get update && apt-get install -y build-essential python && \
wget archive.apache.org/dist/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz && \
tar -xzvf hadoop-3.1.1.tar.gz && \
mv hadoop-3.1.1 /user/local/hadoop && \
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.1.jar wordcount /usr/local/hadoop/LICENSE.txt ~/output && \
cat ~/output/part-r-*

# export JAVA_HOME=/usr/lib/jvm/java-8-oracle/jre

