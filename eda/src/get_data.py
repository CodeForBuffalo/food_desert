import pandas as pd

farmers_markets = pd.read_csv('https://data.ny.gov/api/views/xjya-f8ng/rows.csv?accessType=DOWNLOAD')
farmers_markets.to_csv('../data/raw/farmers_markets.csv')


food_stores = pd.read_csv('https://data.ny.gov/api/views/9a8c-vfzj/rows.csv?accessType=DOWNLOAD')
food_stores.to_csv('../data/raw/food_stores.csv')
