#load example file
hadoop_rdd = sc.textFile('/dis_materials/hadoop_1m.txt')
hadoop_rdd = sc.textFile('file:///root/dis_materials/hadoop_1m.txt')

#count number of like and display first 5 lines
hadoop_rdd.count()
hadoop_rdd.take(5)

#count email domains
#compare to Hadoop code from earlier lectures
domain_counts = (hadoop_rdd
                 .filter(lambda line: line.find("From:") == 0)
                 .map(lambda line: (line[line.find("@")+1:line.find(">")],1))
                 .reduceByKey(lambda a, b: a+b))

domain_counts.count()
domain_counts.take(5)

#Comapre reduceByKey to reduce
#domain_counts above finishes with reduce, we see below that the result of such operation is an RDD, so it's a transformation
#If we run reduce on domain_counts it becomes just a number which is returned to the driver, so it's an action, like take or count above

domain_counts
domain_counts.map(lambda (a, b): b).reduce(lambda a, b: a+b)

#Load library and data for SPARK SQL
from pyspark.sql import SQLContext, Row
sqlContext = SQLContext(sc)
hadoop_csv_rdd = sc.textFile('/dis_materials/hadoop_1m.csv')

emails = (hadoop_csv_rdd
         .map(lambda l: l.split(","))
         .map(lambda p: Row(id=p[0], list=p[1], date1=p[2], date2=p[3], email=p[4], subject=p[5])))

emails.take(5)

schemaEmails = sqlContext.createDataFrame(emails)
schemaEmails.registerTempTable("emails")

#run sample query
lists = sqlContext.sql("SELECT COUNT(DISTINCT(email)) FROM emails")
lists.collect()