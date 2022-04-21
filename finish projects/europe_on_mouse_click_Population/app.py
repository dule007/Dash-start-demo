import geojson
import pandas as pd
import dash
from dash import Input,Output,dcc,html
import plotly.graph_objects as go
import json
import urllib.request
import random




def read_gejosn_2(path_to_file):
    with open(path_to_file) as f:
        gj = geojson.load(f)
    return gj 

file_f = 'europe.geojson'

jdata = read_gejosn_2(file_f)
thelist = jdata['features']
locations =  [ item['id'] for item in thelist ] 

population = []
for i in range(0,50):
    
    population.append(jdata['features'][i]['properties']['POP2005'])

z = population

mapboxt = open("mapbox_token.txt").read().rstrip() #my mapbox_access_token  must be used only for special mapbox style
app = dash.Dash()

fig= go.Figure(go.Choroplethmapbox(z=z, # This is the data.
                            locations=locations,
                            colorscale='reds',
                            colorbar=dict(thickness=20, ticklen=3),
                            geojson=jdata,
                            text=locations,
                            hoverinfo='all',
                            marker_line_width=1, marker_opacity=0.75))
                            
                            
fig.update_layout(title_text= 'Symptom Map',
                  title_x=0.5, width = 700,height=700,
                  mapbox = dict(center= dict(lat=43.9159,  lon=17.6791),
                                 accesstoken= mapboxt,
                                 style='basic',
                                 zoom=5.6,
                               ));




app.layout = html.Div([
    dcc.Graph(id='map-plot',figure=fig),
    html.Div([
    html.H1(id='hover-data', style={'paddingTop':35})
    ], style={'position': 'absolute','top': '8px','right': '16px','font-size': '18px'})
])
@app.callback(
    Output('hover-data', 'children'),
    [Input('map-plot', 'hoverData')])
def callback_image(hoverData):
    #print("TESTNI ISPIS :::::::::::::::::   ",hoverData['POP2005'],"  ::::::::::::::: KRAJ TESTNOG ISPISA")
    #print("TYPE ::: ",type(hoverData),hoverData['points'][0]['z'])
    return json.dumps(hoverData['points'][0]['z'], indent=2)

if __name__ == '__main__':
    app.run_server(debug=True)