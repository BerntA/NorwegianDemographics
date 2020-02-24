#!/bin/bash

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar \
    -mapper $1 \
    -reducer $2 \
    -input $3 \
    -output $4 \
    -file $1 \
    -file $2
