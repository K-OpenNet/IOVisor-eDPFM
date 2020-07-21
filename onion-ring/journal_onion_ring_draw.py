#url : 127.0.0.1
import plotly.graph_objects as go
import time
import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask

app = dash.Dash(__name__)
server = flask.Flask(__name__)
app=dash.Dash(__name__,server=server)

test_value1 = 14
test_value2 = 2

mid_val3 = [0,0,0]

# define colors codes here
RED = "#ff0000"
DARK_GREEN = "#006400"
GREEN = "#099441"
LIGHT_GREEN = "#60a830"
YELLOW_GREEN = "d9df1d"
BLACK = "#000000"
WHITE = "#FFFFFF"
GRAY = "#808080"
SILVER = "#C0C0C0"
YELLOW = "#FFFF00"
FOREST_GREEN = "#228B22"
LIME = "#F4FF00"


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

def define_color(input):
    input = int(input)
    if input < 100 :
        return YELLOW_GREEN
    elif input >=100 and input < 200:
        return LIME
    elif input >=200 and input < 400:
        return YELLOW
    elif input >=400 and input < 600:
        return LIGHT_GREEN
    elif input >=600 and input < 800:
        return DARK_GREEN
    else:
        return RED

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

    f = open('cube1_eno1.txt', 'r')
    cube1_1 = f.read()
    col_cube1_eno1 = define_color(cube1_1)
    f.close()

    f = open('cube1_eno2.txt', 'r')
    cube1_2 = f.read()
    col_cube1_eno2 = define_color(cube1_2)
    f.close()

    f = open('cube1_eno7.txt', 'r')
    cube1_7 = f.read()
    col_cube1_eno7 = define_color(cube1_7)
    f.close()

    # place for cube1_3 (add cube1_3 below too)
    col_cube1_eno3 = LIME

    col_cube1 = define_color(int(cube1_1)+int(cube1_2)+int(cube1_7))

    f = open('cube2_eno1.txt', 'r')
    cube2_1 = f.read()
    col_cube2_eno1 = define_color(cube2_1)
    f.close()

    f = open('cube2_eno2.txt', 'r')
    cube2_2 = f.read()
    col_cube2_eno2 = define_color(cube2_2)
    f.close()

    f = open('cube2_eno7.txt', 'r')
    cube2_7 = f.read()
    col_cube2_eno7 = define_color(cube2_7)
    f.close()

    # place for cube2_3 (add cube2_3 below too)
    col_cube2_eno3 = LIME

    col_cube2 = define_color(int(cube2_1)+int(cube2_2)+int(cube2_7))

    f = open('cube3_eno1.txt', 'r')
    cube3_1 = f.read()
    col_cube3_eno1 = define_color(cube3_1)
    f.close()

    f = open('cube3_eno2.txt', 'r')
    cube3_2 = f.read()
    col_cube3_eno2 = define_color(cube3_2)
    f.close()

    # place for cube3_3 (add cube3_3 below too)
    f = open('cube3_eno7.txt', 'r')
    cube3_7 = f.read()
    col_cube3_eno7 = define_color(cube3_7)
    f.close()

    col_cube3 = define_color(int(cube3_1)+int(cube3_2)+int(cube3_7))

    f = open('cube4_eno1.txt', 'r')
    cube4_1 = f.read()
    col_cube4_eno1 = define_color(cube4_1)
    f.close()

    f = open('cube4_eno2.txt', 'r')
    cube4_2 = f.read()
    col_cube4_eno2 = define_color(cube4_2)
    f.close()

    f = open('cube4_eno7.txt', 'r')
    cube4_7 = f.read()
    col_cube4_eno7 = define_color(cube4_7)
    f.close()

    col_cube4 = define_color(int(cube4_1)+int(cube4_2)+int(cube4_7))

    # Place for cube5

    f = open('cube5_eno1.txt', 'r')
    cube5_1 = f.read()
    col_cube5_eno1 = define_color(cube5_1)
    f.close()

    f = open('cube5_eno2.txt', 'r')
    cube5_2 = f.read()
    col_cube5_eno2 = define_color(cube5_2)
    f.close()

    f = open('cube5_eno7.txt', 'r')
    cube5_7 = f.read()
    col_cube5_eno7 = define_color(cube5_7)
    f.close()

    col_cube5 = define_color(int(cube5_1)+int(cube5_2)+int(cube5_7))

    # input source for data - END
    fig = go.Figure(go.Sunburst(
    textfont = {"size":15},
    labels=[" ","K-Fabric","K-Cube1","K-Cube2","K-Cube3","K-Cube4","K-Cube5","eno1","eno2","eno3","eno1  ","eno2  ","eno3  ","eno1 ","eno2 ","eno3 ","eno1   ","eno2   ","eno3   ","eno1    ","eno2    ","eno3    ","vSW1","vSW2","vSW3","VM1","VM2","VM3","vSW1 ","vSW2 ","vSW3 ","VM1 ","VM2 ","VM3 "],#9
# all the settings below probably follows the order of the labels above

parents=[""," ","K-Fabric","K-Fabric","K-Fabric","K-Fabric","K-Fabric","K-Cube1","K-Cube1","K-Cube1","K-Cube2","K-Cube2","K-Cube2","K-Cube3","K-Cube3","K-Cube3","K-Cube4","K-Cube4","K-Cube4","K-Cube5","K-Cube5","K-Cube5","eno1    ","vSW1","vSW1","vSW3","vSW3","vSW2","eno1","vSW1 ","vSW1 ","vSW3 ","vSW3 ","vSW2 ",],
# values = [BPF2, BPF3, BPF1] : BFP1 size doesn't really change

marker = {"colors":[WHITE,WHITE,col_cube1,col_cube2,col_cube3,col_cube4,col_cube5,col_cube1_eno1,col_cube1_eno2,col_cube1_eno7,col_cube2_eno1,col_cube2_eno2,col_cube2_eno7,col_cube3_eno1,col_cube3_eno2,col_cube3_eno7,col_cube4_eno1,col_cube4_eno2,col_cube4_eno7,col_cube5_eno1,col_cube5_eno2,col_cube5_eno7,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,],
        "line":{'color':[BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,]}}, # in the order of BPF2, BPF3
        
        ))  # set row / col here
#    fig.update_layout(grid=dict(columns=1,rows=1),margin = dict(t=0, l=0, r=0, b=0)) # maybe this is where they change the subplot
    f.close()
    return fig

go.visible = False

app.run_server(debug=True, host='210.117.251.25')

#kafka_consumer()
