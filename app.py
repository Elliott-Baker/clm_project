import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html

csv_path =  'https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/companies.csv'
#csv_path = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'
column_names = ['Company Change', 'Percent Change']
#df = pd.read_csv('https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/companies.csv')
df = pd.read_csv(csv_path, usecols=column_names)
print(df)

fig = go.Figure(data=[go.Scatter(x=df['AAPL_x'], y=df['AAPL_y'])])

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)