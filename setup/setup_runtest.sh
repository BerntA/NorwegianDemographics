#!/bin/bash
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.1.jar wordcount /usr/local/hadoop/LICENSE.txt ~/output && \
cat ~/output/part-r-*
