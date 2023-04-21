import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html

stocks_path = 'https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/s%26p500.csv'
stocks_column_names = ['x', 'Percent Change', 'Company Name']

colors = {
    'background': '#f5f5f5',
    'text': '#1e90ff'
}

stock_frame = pd.read_csv(stocks_path, usecols=stocks_column_names)

fig = go.Figure(go.Histogram(x=stock_frame['Percent Change'], xbins=dict(start=-0.0566, end=0.0566, size=0.001), autobinx=False))
                                   
fig.update_layout(
    xaxis_title_text='Percent Change', # xaxis label
    yaxis_title_text='Count', # yaxis label
    plot_bgcolor=colors['background'], # plot background color
    paper_bgcolor=colors['background'], # paper background color
    font_color=colors['text'] # font color
)

app = dash.Dash()
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
    children='S&P 500', 
    style={
        'textAlign': 'center',
        'color': colors['text']
        }
    ),

    html.Div(children='This histogram shows the distribution of the percent change of all 500 stocks in the S&P500 index on a given day.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(figure=fig)
])

app.run_server(debug=True)