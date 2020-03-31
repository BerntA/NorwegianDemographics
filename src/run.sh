#!/bin/bash

# Run preprocessing on raw data. Clean the data.
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -file /home/ubuntu/dat500/src/preprocess_mapper.py -mapper preprocess_mapper.py -file /home/ubuntu/dat500/src/preprocess_reducer.py -reducer preprocess_reducer.py -input /data/census.csv -output /output/preprocessed && \

# Run cleaned data through MRJob or Spark

