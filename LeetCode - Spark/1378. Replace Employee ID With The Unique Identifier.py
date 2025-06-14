# 1378. Replace Employee ID With The Unique Identifier

data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
data = [[3, 1], [11, 2], [90, 3]]
employee_uni = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})

employees_df = spark.createDataFrame(employees)
employee_uni_df = spark.createDataFrame(employee_uni)

df = employees_df\
    .join(employee_uni_df, employees_df.id == employee_uni_df.id,"left")\
        .select(employee_uni_df.unique_id, employees_df.name)

df.display()