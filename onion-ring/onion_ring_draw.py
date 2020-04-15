#url : 127.0.0.1
import plotly.graph_objects as go
import time
import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

test_value1 = 14
test_value2 = 2

mid_val3 = [0,0,0]

# define colors codes here
RED = "#ff0000"
DARK_GREEN = "#224d17"
GREEN = "#099441"
LIGHT_GREEN = "#60a830"
YELLOW_GREEN = "d9df1d"
BLACK = "#000000"
WHITE = "#FFFFFF"
GRAY = "#808080"
SILVER = "#C0C0C0"
YELLOW = "#FFFF00"

# define parameter values for coloring
LEVEL0 = 0
LEVEL1 = 10
LEVEL2 = 15
LEVEL3 = 20
LEVEL4 = 25
LEVEL5 = 30
LEVEL6 = 35

# define level colors here

LEVEL0_COL = GRAY
LEVEL1_COL = YELLOW_GREEN
LEVEL2_COL = LIGHT_GREEN
LEVEL3_COL = GREEN
LEVEL4_COL = DARK_GREEN
LEVEL5_COL = RED
        
COLOR1 = WHITE
test_value1 = 2
test_value2 = 34
            
bpf2_color = GRAY
bpf3_color = RED

# Each arguments below have to be assigned only a single time. IF NOT -> ERROR
#    fig = go.Figure()
#    fig = make_subplots(1,2,specs=[[{"type":"domain"},{"type":"domain"}]],)
# input (cols, rows) above 
#            if (test_value1 > 50):
#    fig.show()

app = dash.Dash()

app.layout = html.Div([
    html.H1(children='upper'),
    dcc.Graph(id='live-update-graph',animate=True),
    dcc.Interval(
        id = 'interval-component',
        interval = 3 * 1000,
        n_intervals = 0
        ),
    html.H1(children="under")])

@app.callback(Output('live-update-graph', 'figure'),
        [Input('interval-component', 'n_intervals')])

def update_graph_live(n):
    # input source for data - BEGIN

    f = open('color.txt', 'r')
    temp_color = f.read()
    
    # input source for data - END
    fig = go.Figure(go.Sunburst(
    textfont = {"size":15},
    labels=[" ","kube_master","kube_1","kube_2","edgebox1","edgebox2","vm1","vm2","vm3","vm4","vm5","  ","    ","       "],
# all the settings below probably follows the order of the labels above
    
    parents=[""," "," "," "," "," ","edgebox2","edgebox2","edgebox2","edgebox1","edgebox1","kube_1","kube_2","kube_master"],
# values = [BPF2, BPF3, BPF1] : BFP1 size doesn't really change

    marker = {"colors":[temp_color,YELLOW,YELLOW,YELLOW,YELLOW,YELLOW,RED,RED,RED,RED,RED,WHITE,WHITE,WHITE],
        "line":{'color':[BLACK]}}, # in the order of BPF2, BPF3
        ))  # set row / col here
#    fig.update_layout(grid=dict(columns=1,rows=1),margin = dict(t=0, l=0, r=0, b=0)) # maybe this is where they change the subplot
    f.close()
    return fig

go.visible = False

app.run_server(debug=True)

#kafka_consumer()
