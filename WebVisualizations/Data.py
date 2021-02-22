import pandas as pd
cities = pd.read_csv("../Resources/cities.csv")
cities.set_index('City_ID', inplace=True)
cities.to_html("../Resources/cities.html")