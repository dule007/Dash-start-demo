import geojson
import pandas as pd
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objects as go
import json
import urllib.request
import random


def read_geojson(url):
    with urllib.request.urlopen(url) as url:
        jdata = json.loads(url.read().decode())
    return jdata 

#irish_url = 'https://gist.githubusercontent.com/pnewall/9a122c05ba2865c3a58f15008548fbbd/raw/5bb4f84d918b871ee0e8b99f60dde976bb711d7c/ireland_counties.geojson'

#jdata = read_geojson(irish_url)
def read_gejosn_2(path_to_file):
    with open(path_to_file) as f:
        gj = geojson.load(f)
    return gj 

file_f = 'data/test2.geojson'

jdata = read_gejosn_2(file_f)
print(jdata)
thelist = jdata['features']
print("     THE LIST :::::: ",thelist)
print("00000000000000000000000000000000000000000000000")
locations =  [ item['id'] for item in thelist ] 

print("     THE LIST ->>>> idds :::::: ",locations)
# thelist = jdata['features']
# locations =  [ item['id'] for item in thelist ] 
# print('locations: ', locations)

randomlist = []
for i in range(0,26):
    n = random.randint(0,10)
    randomlist.append(n)

z = randomlist

print('z: ', z)
mapboxt = open("data/mapbox_token.txt").read().rstrip() #my mapbox_access_token  must be used only for special mapbox style
print('mapboxt: ', mapboxt)

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

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)