import os
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('withColumn').master('local[*]').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('error')

data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]

cols = ["firstname","lastname","country","state"]

df = spark.createDataFrame(data, cols)
#df.show()

df2 = df.select("firstname","state","country")
df2.show()


