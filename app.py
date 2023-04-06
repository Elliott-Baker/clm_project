import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html

df = pd.read_csv('https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/companies.csv')
fig = go.Figure(data=[go.Histogram(x=df['Percent Change'])])

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)