#!/usr/bin/python3

from pyspark.sql import SQLContext, Row, SparkSession
from collections import Counter

spark = SparkSession.builder.appName('CensusAnalysis').getOrCreate()
sc = spark.sparkContext

sqlContext = SQLContext(sc)
df_census = sc.textFile('/data/census_preprocessed.csv')
people = (df_census.map(lambda l: l.split(",")).map(lambda p: Row(municipality=p[0],gender=p[1],work=p[2],religion=p[4]))) # This is the data we're interested in.

# Create our dataframe.
schemaPeople = sqlContext.createDataFrame(people)
schemaPeople.registerTempTable("people")

# Create output with the top 20 religions in focus, the output contains data about their municipality religion and a count of how many 'members'.
excluded_religions = set(['norwegian church', '?'])
common_religions = Counter(sqlContext.sql("SELECT religion FROM people").collect()).most_common(20) # Select all religions and find the X most common ones!
common_religions = set([k.religion for k,_ in common_religions if k.religion.lower() not in excluded_religions and len(k.religion) > 0])
schemaPeople.filter(schemaPeople.religion.isin(common_religions)).groupBy('municipality', 'religion').count().orderBy("municipality").write.csv('/output/analyze_religion')

# Field of Work, find the top field of work and how they are distributed around Norway!
common_work = set(['Farmer', 'Fisher', 'Housewife', 'Maid']) # Popular field of work, discovered by running a select of all work and counting the frequencies.
schemaPeople.filter(schemaPeople.work.isin(common_work)).groupBy('municipality', 'work').count().orderBy("municipality").write.csv('/output/analyze_work')

# Gender split
schemaPeople.groupBy('municipality', 'gender').count().orderBy("municipality").write.csv('/output/analyze_gender')

spark.stop() # exit, finito.
spark = None
sc = None