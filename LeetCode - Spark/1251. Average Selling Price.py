# 1251. Average Selling Price

import pandas as pd
from pyspark.sql.functions import expr,lit

data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15],
        [2, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype(
    {'product_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]', 'price': 'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype(
    {'product_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'units': 'Int64'})

prices_df = spark.createDataFrame(prices)
units_sold_df = spark.createDataFrame(units_sold)

result_df = units_sold_df.alias("usd")\
    .join(prices_df.alias("price").hint("range_join", 0.5),(expr("usd.product_id = price.product_id")) & (col("usd.purchase_date").between(col("price.start_date"),col("price.end_date"))),"inner")\
        .groupby(col("usd.product_id"))\
            .agg((sum(col("usd.units")*col("price.price")).alias("line_amount")/ sum("usd.units")).cast(DecimalType(10,2)).alias("average_price"))

result_df.display()