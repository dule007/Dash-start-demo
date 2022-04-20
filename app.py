import geojson
import pandas as pd
import dash
from dash import dcc,html
import plotly.graph_objects as go
import json
import urllib.request
import random


import geopandas
from urllib.request import urlopen


with urlopen("https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson") as response:
 Brazil = json.load(response) # Javascrip object notation 
#print(Brazil)
state_id_map = {}
for feature in Brazil ['features']:

    feature['id'] = feature['properties']['name']
    state_id_map[feature['properties']['sigla']] = feature['id']


print(state_id_map)
# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)