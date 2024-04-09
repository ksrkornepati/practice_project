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

data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

cols = ["firstname","middlename","lastname","dob","gender","salary"]

df = spark.createDataFrame(data, cols)
df.show()

cols_to_be_rename = [('firstname', 'fname'),
                     ('middlename', 'mname'),
                     ('lastname', 'lname'),
                     ('dob', 'dateOfBirth'),
                     ('gender', 'Gend'),
                     ('salary', 'sal')]

for i in cols_to_be_rename:
  df = df.withColumnRenamed(i[0], i[1])

df.show()