import dash
from dash import Input,Output,html,dcc
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import numpy as np
import json

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px






fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
if __name__ == '__main__':
    app.run_server()