# 197. Rising Temperature

from pyspark.sql.types import DateType
from pyspark.sql.functions import col, datediff

data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})

weather_df = spark.createDataFrame(weather)

weather_df = weather_df\
    .withColumn("recordDate", col("recordDate").cast('date'))

weather_df = weather_today.alias("today")\
    .join(weather_yesterday.alias("yesterday"), how="cross")\
        .withColumn("datediff", datediff("today.recordDate","yesterday.recordDate"))\
            .filter((datediff(col("today.recordDate"),col("yesterday.recordDate"))==1) & (col("today.temperature") > col("yesterday.temperature")))\
                .select(col("today.id"))

weather_df.display()