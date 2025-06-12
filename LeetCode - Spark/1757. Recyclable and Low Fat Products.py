import pandas as pd

data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})

products = spark.createDataFrame(products)

products = products.alias('prod')\
    .filter((products.recyclable=='Y') & (products.low_fats=='Y'))\
        .select(products.product_id)

products.display()