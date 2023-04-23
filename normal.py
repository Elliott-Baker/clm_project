import plotly.graph_objects as go
import dash
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from dash import dcc, html
from plotly.subplots import make_subplots

stocks_path = 'https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/s%26p500.csv'
stocks_column_names = ['x', 'Percent Change', 'Company Name']
stock_frame = pd.read_csv(stocks_path, usecols=stocks_column_names)

mean = stock_frame['Percent Change'].mean()
std_dev = stock_frame['Percent Change'].std()
cdf = stats.norm.cdf(stock_frame['Percent Change'], 0, 1)

fig = go.Figure(go.Scatter(x=[mean, mean], y=[0, 2], mode='lines', name='Mean'))

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
