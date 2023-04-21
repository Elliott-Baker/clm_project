import plotly.graph_objects as go
import plotly.tools as tls
import dash
import numpy as np
import pandas as pd
import statsmodels.api as sm
from dash import dcc, html

stocks_path = 'https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/s%26p500.csv'
stocks_column_names = ['x', 'Percent Change', 'Company Name']
stock_frame = pd.read_csv(stocks_path, usecols=stocks_column_names)

# create qq plot of percent change with 45-degree line
qq = sm.qqplot(stock_frame['Percent Change'], line='45', fit=True)

fig = tls.mpl_to_plotly(qq)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)