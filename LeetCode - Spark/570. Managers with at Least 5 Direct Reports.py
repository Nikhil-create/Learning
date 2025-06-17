# 570. Managers with at Least 5 Direct Reports

from pyspark.sql.functions import countDistinct

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

employee = spark.createDataFrame(employee)

result_df = employee.alias("emp")\
    .join(employee.alias("man"), col("emp.managerId")==col("man.id"),"inner")\
        .groupBy(col("man.id"), col("man.name"))\
            .agg(countDistinct(col("emp.id")).alias("directReporte"))\
                .filter(col("directReporte")>= 5)\
                    .select(col("man.name"))

result_df.display()
