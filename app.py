import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html

csv_path = 'https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/s%26p500.csv'
#csv_path = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'
column_names = ['x', 'Percent Change', 'Company Name']
#df = pd.read_csv('https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/companies.csv')

df = pd.read_csv(csv_path, usecols=column_names)

fig = go.Figure(data=[go.Histogram(x=df['Percent Change'], 
                                   xbins=dict(
                                        start=-0.0566,
                                        end=0.0566,
                                        size=0.01),
                                     autobinx=False
                                     )])
                                   

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)