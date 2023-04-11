import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html

csv_path = 'https://raw.githubusercontent.com/Elliott-Baker/clm_project/master/datasets/s%26p500.csv'
column_names = ['x', 'Percent Change', 'Company Name']

colors = {
    'background': '#f5f5f5',
    'text': '#1e90ff'
}

df = pd.read_csv(csv_path, usecols=column_names)

fig = go.Figure(data=[go.Histogram(x=df['Percent Change'], 
                                   xbins=dict(
                                        start=-0.0566,
                                        end=0.0566,
                                        size=0.001),
                                     autobinx=False
                                     )])
                                   
fig.update_layout(
    title_text='Percent Change of S&P 500', # title of plot
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