# 1661. Average Time of Process per Machine
from pyspark.sql.functions import avg, round

data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]

activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})

activity = spark.createDataFrame(activity)

activity = activity\
    .alias("act_start")\
        .join(activity.alias("act_end"),(col("act_start.machine_id")==col("act_end.machine_id")) & (col("act_start.process_id")== col("act_end.process_id")), how="inner")\
            .filter((col("act_start.activity_type")=='start') & (col("act_end.activity_type")=='end'))\
                .withColumn("processingTime", col("act_end.timestamp") - col("act_start.timestamp"))\
                    .groupBy(col("act_start.machine_id"))\
                        .agg(round(avg(col("processingTime")),3))

activity.display()
