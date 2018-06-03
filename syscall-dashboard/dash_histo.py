import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import defaultdict
import signal
import numpy as np
import sys
import json
import re
import threading
import time
import operator
import argparse
import logging

from dash.dependencies import Input, Output

style = {'padding': '5px', 'fontSize': '32px'}

app = dash.Dash(__name__)
app.layout = html.Div(
    html.Div([
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds
            n_intervals=0
        )
    ])
)

bins = defaultdict(lambda: 0)

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    total = reduce(operator.add, bins.values(), 0)
    uniq = len(bins)
    style = {'padding': '5px', 'fontSize': '32px'}
    return [
        html.Div('Total count: {0:d}'.format(total), style=style),
        html.Div('Unique "syscall(fd)": {0:d}'.format(uniq), style=style),
    ]

p = re.compile(r'fd=([0-9]+)')

def update_bins():
    fifo = sys.stdin
    while True:
        try:
            line = fifo.readline()
            if not line:
                break
            syscall = json.loads(line)
            if len(syscall) == 0:
                continue
            for key, value in syscall.iteritems():
                bins[key] = value
        except (ValueError, KeyError):
            pass
        except IOError:
            sys.exit(0)


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    return go.Figure(
        data=[
            go.Bar(
                x=bins.keys(),
                y=bins.values(),
                name='syscall[fd] count',
            )
        ],
        layout=go.Layout(
            title='Count',
            margin=go.Margin(l=100, r=50, t=40, b=200),
            height='150px',
            autosize=True,
            font=dict(family='Courier New, monospace', size=20)
        )
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        dest='port',
        nargs='?',
        default=8050)
    args = parser.parse_args()

    t = threading.Thread(target=update_bins)
    t.daemon = True
    t.start()
    app.run_server(debug=False, port=args.port)
