import plotly.graph_objects as go
import plotly.tools as tls
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

# initialize figure with two subplots
fig = make_subplots(rows=1, cols=2, subplot_titles = ('QQ Plot', 'Histogram'))

# create qq plot of percent change with 45-degree line
qqplot_data = sm.qqplot(stock_frame['Percent Change'], line='s').gca().lines
trace1 = go.Scatter(x=qqplot_data[0].get_xdata(), y=qqplot_data[0].get_ydata(), mode='markers', name='Percent Change')
trace2 = go.Scatter(x=qqplot_data[1].get_xdata(), y=qqplot_data[1].get_ydata(), mode='lines', name='45 Degree Line')
fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=1, col=1)

# create histogram of percent change
fig.add_trace(go.Histogram(x=stock_frame['Percent Change'], xbins=dict(start=-0.0566, end=0.0566, size=0.001), autobinx=False), row=1, col=2)

# create normal curve to overlay on histogram
mu, std = stats.norm.fit(stock_frame['Percent Change'])
x = np.linspace(-0.06, 0.06, 1000)
y = stats.norm.pdf(x, mu, std)*len(stock_frame)*0.001
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Curve'), row=1, col=2)

# update qq plot axis properties
fig.update_xaxes(title_text="Theoretical Quantiles", row=1, col=1)
fig.update_yaxes(title_text="Sample Quantiles", row=1, col=1)

# update histogram axis properties
fig.update_xaxes(title_text="Percent Change", row = 1, col = 2)
fig.update_yaxes(title_text="Frequency", row = 1, col = 2)

fig.update_layout(showlegend=False, height=600, width=1500)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='S&P 500 Percent Change Analysis', style={'textAlign': 'center'}),
    html.Div(children='This is a simple analysis of the normal distribution of S&P 500 percent change data from a given day. On the left is a Q-Q plot, which shows theoretical quantiles in comparison to the sample quantiles. The closer the blue scatter plot follows the red line, the closer the sample is to being normally distributed. Similarly, on the right a histogram is displayed, which shows a normal looking plot.', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
