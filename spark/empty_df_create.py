import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('empty DF create').master('local[*]').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('error')

cols = 'name string, id int, dept string'

df = spark.createDataFrame([], cols)
df.show()