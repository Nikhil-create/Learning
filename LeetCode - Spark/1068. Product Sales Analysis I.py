# 1068. Product Sales Analysis I

data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})
data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype({'product_id':'Int64', 'product_name':'object'})


sales_df = spark.createDataFrame(sales)
product_df = spark.createDataFrame(product)

df = sales_df\
    .join(product_df, sales_df.product_id == product_df.product_id,"left")\
        .select(product_df.product_name, sales_df.year,sales_df.price)

df.display()