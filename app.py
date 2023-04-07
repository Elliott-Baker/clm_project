import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html

csv_path =  'https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/numbers.csv'
column_names = ['x', 'y']
#df = pd.read_csv('https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/companies.csv')
df = pd.read_csv(csv_path, usecols=column_names)
print(df)

fig = go.Figure(data=[go.Scatter(x=df['x'], y=df['y'])])

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)