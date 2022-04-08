import dash
from dash import Input,Output,html,dcc
import pandas as pd
import numpy as np


app = dash.Dash()

df = pd.read_csv('data/wheels.csv')

app.layout = html.Div([ 



])


if __name__ == '__main__':
    app.run_server()