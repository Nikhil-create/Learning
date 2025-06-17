# 1934. Confirmation Rate

import pandas as pd
from pyspark.sql.functions import sum, count, round
from pyspark.sql.types import DecimalType

# Other alternative of round is, DecimalType , format_number (convert number to string)

data = [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'], [6, '2020-12-09 10:39:37']]
signups = pd.DataFrame(data, columns=['user_id', 'time_stamp']).astype(
    {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})
data = [[3, '2021-01-06 03:30:46', 'timeout'], [3, '2021-07-14 14:00:00', 'timeout'],
        [7, '2021-06-12 11:57:29', 'confirmed'], [7, '2021-06-13 12:58:28', 'confirmed'],
        [7, '2021-06-14 13:59:27', 'confirmed'], [2, '2021-01-22 00:00:00', 'confirmed'],
        [2, '2021-02-28 23:59:59', 'timeout']]
confirmations = pd.DataFrame(data, columns=['user_id', 'time_stamp', 'action']).astype(
    {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]', 'action': 'object'})

signups_df = spark.createDataFrame(signups)
confirmations_df = spark.createDataFrame(confirmations)

results_df = signups_df.alias("signup")\
    .join(confirmations_df.alias("confirm"), col("signup.user_id")==col("confirm.user_id"),how="left")\
        .groupBy(col("signup.user_id"))\
            .agg(sum(when(col("confirm.action")=="confirmed",1).otherwise(0)).alias("confirmedCount")\
                ,when(count(col("confirm.action"))==0,1).otherwise(count(col("confirm.action"))).alias("requestedCount"))\
                    .withColumn("confirmation_rate",round(col("confirmedCount")/col("requestedCount"),2).cast(DecimalType(10,2)))\
                        .select(col("signup.user_id"),col("confirmation_rate"))

results_df.display()
