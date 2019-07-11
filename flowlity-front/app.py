# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

COLORS = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(
        children='Flowlity Exercise',
        style={
            'textAlign': 'center',
            'color': COLORS['text'],
        }
    ),

    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    dcc.Graph(
        id='inventory-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Inventory per date'
            }
        }
    ),

    html.Table([
        html.Tr([
            html.Th("Id"), html.Th("Name"), html.Th("Date"), html.Th("Inventory level")
        ]),
        html.Tr([
            html.Td(12), html.Td("Cow"), html.Td("2019-05-26"), html.Td(15623)
        ])
    ]),

    dash_table.DataTable(
        id='table',
        columns=[
            {"name": "Id", "id": 1},
            {"name": "Name", "id": 2},
            {"name": "Date", "id": 3},
            {"name": "Inventory Level", "id": 4},
        ],
        data=[
            {1: 45, 2: "cow", 3: "2019-08-12", 4: 6876}
        ],
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
