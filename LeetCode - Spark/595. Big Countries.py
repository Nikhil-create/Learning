# 595. Big Countries

# Pandas Schema
import pandas as pd

data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000],
        ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000],
        ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
world = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
    {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})

world_df = spark.createDataFrame(world)

world_df = world_df.filter((world_df.area >= 3000000) | (world_df.population >= 25000000))\
    .select(world_df.name, world_df.area, world_df.population)

world_df.display()