# 620. Not Boring Movies

import pandas as pd
from pyspark.sql.functions import desc

data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2],
        [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype(
    {'id': 'Int64', 'movie': 'object', 'description': 'object', 'rating': 'Float64'})

cinema_df = spark.createDataFrame(cinema)

cinema_df = cinema_df.filter((col("id")%2==1) & (col("description")!="boring"))\
    .orderBy(col("rating").desc())

cinema_df.display()

