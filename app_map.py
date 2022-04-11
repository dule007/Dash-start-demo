import dash
from dash import Input,Output,html,dcc
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json


app = dash.Dash()

df = pd.read_csv('data/wheels.csv')

app.layout = html.Div([ 

    html.Div(
        dcc.Graph(id='wheels-plot',
                  figure = {'data':[go.Scatter(
                                    x = df['color'],
                                    y = df['wheels'],
                                    dy = 1,
                                    mode = 'markers',
                                    marker = {'size':15}

                  )],
                            'layout': go.Layout(title='Test',hovermode='closest')}
        )
    ),
    html.Div(
        html.Pre(id='hover-data',style={'paddingTop':35}),
        style={'width':'30%'}
    )

])

@app.callback(Output('hover-data','children'),

             [Input('wheels-plot','hoverData')]

            )
def callback_image(hoverData):
    return json.dumps(hoverData,indent=2)

if __name__ == '__main__':
    app.run_server()