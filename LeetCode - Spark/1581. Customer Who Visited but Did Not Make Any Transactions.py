
# Customer Who Visited but Did Not Make Any Transactions
from pyspark.sql.functions import length, count

data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
visits = pd.DataFrame(data, columns=['visit_id', 'customer_id']).astype({'visit_id':'Int64', 'customer_id':'Int64'})

visits_df = spark.createDataFrame(visits)

data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
transactions = pd.DataFrame(data, columns=['transaction_id', 'visit_id', 'amount']).astype({'transaction_id':'Int64', 'visit_id':'Int64', 'amount':'Int64'})

transactions_df = spark.createDataFrame(transactions)

df = visits_df\
    .join(transactions_df, visits_df.visit_id == transactions_df.visit_id,"left")\
        .filter((transactions_df.transaction_id.isNull()))\
            .groupBy(visits_df.customer_id)\
                .agg(count(visits_df.visit_id).alias("count_no_trans"))

df.display()