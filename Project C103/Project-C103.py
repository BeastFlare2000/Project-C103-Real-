import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
date = df['date'].tolist()
cases = df['cases'].tolist()
data = px.scatter(x=date,y=cases)
data.show()