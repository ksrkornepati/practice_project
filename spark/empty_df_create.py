import pyspark
from pyspark.sql.functions import *
from pyspark.sql.types import *

import os
import sys
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.getOrCreate()
spark = SparkSession.builder.appName('practice').master('local[*]').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('error')

cols = 'name string, id int, dept string'

df = spark.createDataFrame([],cols)
df.show()