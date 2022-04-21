import csv
import dash
from dash import Input,Output,html,dcc
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import numpy as np
import json
import plotly.express as px

# hover data 

df = pd.read_csv('ba.csv')

# >>city,>>lat,>>lng,country,iso2,>>admin_name,capital,>>population,population_proper


df_map = df
df_map.drop(["country","iso2","capital","population_proper"],axis=1,inplace=True)

#   City,State,Population,lat,lon
coumn_n = ['city','admin_name','population','lat','lng']




fig = px.scatter_mapbox(df_map, lat="lat", lon="lng", hover_name="city", hover_data=["admin_name", "population"],
                        color_discrete_sequence=["blue"],size_max=50, zoom=3)
fig.update_layout(mapbox_style="open-street-map", mapbox = dict(center= dict(lat=43.9159,  lon=17.6791)))
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash()
app.layout = html.Div([
    html.Div([
    dcc.Graph(id='map-plot',figure=fig)
],
style={'height':'500px','width':'60%','background-color':'powderblue'}),


 html.Div([
    html.Pre(id='hover-data', style={'paddingTop':35})
    ], style={'position': 'absolute','top': '8px','right': '16px','font-size': '18px'})
])

@app.callback(
    Output('hover-data', 'children'),
    [Input('map-plot', 'hoverData')])
def callback_image(hoverData):
    print("TESTNI ISPIS :::::::::::::::::   ",hoverData,"  ::::::::::::::: KRAJ TESTNOG ISPISA")
    return json.dumps(hoverData, indent=2)

if __name__ == '__main__':
    app.run_server()



