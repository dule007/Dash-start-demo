import dash_html_components as html
import dash_leaflet as dl
import dash_core_components as dcc
import dash_leaflet.express as dlx
from dash import Dash
from dash.dependencies import Output, Input
from dash_extensions.javascript import assign

# A few cities in Denmark.
cities = [dict(name="Sarajevo", lat=43.8667, lon=18.4167),
          dict(name="Banja Luka", lat=44.7667, lon=17.1833),
          dict(name="Mostar", lat=43.3494, lon=17.8125)]
# Create drop down options.
dd_options = [dict(value=c["name"], label=c["name"]) for c in cities]
dd_defaults = [o["value"] for o in dd_options]
# Generate geojson with a maker for each city and name as tooltip.
geojson = dlx.dicts_to_geojson([{**c, **dict(tooltip=c['name'])} for c in cities])
# Create javascript function that filters on feature name.
geojson_filter = assign("function(feature, context){return context.props.hideout.includes(feature.properties.name);}")
# Create example app.
app = Dash()
app.layout = html.Div([
    dl.Map(children=[
        dl.TileLayer(),
        dl.GeoJSON(data=geojson, options=dict(filter=geojson_filter), hideout=dd_defaults, id="geojson")
    ], 
    style={'width': '50%', 'height': '50vh'}, id="map"),
    dcc.Dropdown(id="dd", value=dd_defaults, options=dd_options, clearable=False, multi=True),
html.Div([
    html.H1(id='number-out',style={'width':'20%'})
])
    
])


# Link drop down to geojson hideout prop (could also be done with a normal callback).
app.clientside_callback("function(x){return x;}", Output("geojson", "hideout"), Input("dd", "value"))



# hover over data 
@app.callback(
    Output('number-out', 'children'),
    [Input("dd", "hoverData")])
def callback_image(hoverData):
    #hoverData =123
    print((hoverData[0]['value']))
    return ' displayed after {} clicks'.format(hoverData[0]['value'])

if __name__ == '__main__':
    app.run_server()