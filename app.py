import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html

df = pd.read_excel('C:/Users/ebake/Documents/stat_3600_project/companies.xlsx')
fig = go.Figure(data=[go.Histogram(x=df['Percent Return'])])

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)