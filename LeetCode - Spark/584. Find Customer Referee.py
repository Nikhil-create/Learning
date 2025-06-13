import pandas as pd
from pyspark.sql.types import StructType,StructField,IntegerType,StringType

data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype(
    {'id': 'Int64', 'name': 'object', 'referee_id': 'Int64'})

schema = StructType([
    StructField('id',IntegerType(),True),
    StructField('name',StringType(), True),
    StructField('referee_id', IntegerType(),True)
]
)

customer = spark.createDataFrame(customer, schema=schema)

customer = customer.filter((customer.referee_id !=2) | (customer.referee_id.isNull()))\
    .select('name')

customer.display()