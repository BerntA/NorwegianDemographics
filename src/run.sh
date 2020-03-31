#!/bin/bash

cd ~/dat500/src

# Run preprocessing on raw data. Clean the data.
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -file /home/ubuntu/dat500/src/preprocess_mapper.py -mapper preprocess_mapper.py -file /home/ubuntu/dat500/src/preprocess_reducer.py -reducer preprocess_reducer.py -input /data/census.csv -output /output/preprocessed && \

# Move the output to our data folder.
hadoop fs -mv -n /output/preprocessed/part* /data/census_preprocessed.csv && \
hadoop fs -rm -r /output/preprocessed && \

# Run cleaned data through MRJob and/or Spark

# Generate info about births, '<birth year>,<municipality>,<count>' ...
python3 analyze_census_births.py --hadoop-streaming-jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -r hadoop hdfs:///data/census_preprocessed.csv --output-dir hdfs:///output/analyze_births --no-output && \
hadoop fs -mv -n /output/analyze_births/part* /data/census_births.csv && \
hadoop fs -rm -r /output/analyze_births && \

# hadoop fs -get /data/census_births.csv ~/dat500/src/data/census_births.csv < copy over result for use in visualization

# Generate info about religions based in certain municipality and how many representatives they had in 19XX.

# Generate info about field of work, visualize where the most common type of work were more popular (geographically).

