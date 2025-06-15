# 577. Employee Bonus

data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype({'empId':'Int64', 'name':'object', 'supervisor':'Int64', 'salary':'Int64'})
data = [[2, 500], [4, 2000]]
bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId':'Int64', 'bonus':'Int64'})

employee_df = spark.createDataFrame(employee)
bonus_df = spark.createDataFrame(bonus)

result = employee_df\
    .alias("emp")\
        .join(bonus_df.alias("bonus"), col("emp.empId")==col("bonus.empId"), how="left")\
            .filter((col("bonus.bonus")< 1000) | col("bonus.bonus").isNull())\
                .select(col("emp.name"), col("bonus.bonus"))

result.display()