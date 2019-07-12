# -*- coding: utf-8 -*-
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import requests
from dash.dependencies import Output, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

COLORS = {
    'background': '#111111',
    'text': '#7FDBFF'
}

dropdown_url = 'http://127.0.0.1:8000/products/all/draw_graph/'
dropdown_data = json.loads(requests.get(dropdown_url).content)
dropdown_options = [{'label': 'All', 'value': 'all'}] \
                   + [{'label': p['name'], 'value': p['id']} for p in dropdown_data]

app.layout = html.Div(children=[
    html.H1(
        children='Flowlity Exercise',
        style={
            'textAlign': 'center',
            'color': COLORS['text'],
        }
    ),

    html.Label('Filter product by name'),
    dcc.Dropdown(
        id='inventory-dropdown',
        options=dropdown_options,
        value='all'
    ),

    dcc.Graph(
        id='inventory-graph',
        figure={
            'data': [],
            'layout': {
                'title': 'Inventory per date'
            }
        }
    ),

    dash_table.DataTable(
        id='inventory-table',
        columns=[],
        data=[],
        style_as_list_view=True,
        style_cell={'padding': '5px'},
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
    )
])


@app.callback(
    Output(component_id='inventory-graph', component_property='figure'),
    [Input(component_id='inventory-dropdown', component_property='value')]
)
def update_graph(input_value):
    url = 'http://127.0.0.1:8000/products/%s/draw_graph/' % input_value
    content = json.loads(requests.get(url).content)
    return {
        'data': content,
        'layout': {
            'title': 'Inventory per date'
        }
    }


@app.callback(
    [Output(component_id='inventory-table', component_property='columns'),
     Output(component_id='inventory-table', component_property='data')],
    [Input(component_id='inventory-dropdown', component_property='value')]
)
def update_table(input_value):
    if input_value == 'all':
        url = 'http://127.0.0.1:8000/products/'
    else:
        url = 'http://127.0.0.1:8000/products/%s' % input_value

    content = json.loads(requests.get(url).content)
    columns = [{'name': k, 'id': k} for k in content[0].keys()]
    return columns, content


if __name__ == '__main__':
    app.run_server(debug=True)
