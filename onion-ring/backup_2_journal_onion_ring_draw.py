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

def define_color(input):
    input = int(input)
    if input < 100 :
        return YELLOW_GREEN
    elif input >=100 and input < 200:
        return YELLOW
    elif input >=200 and input < 400:
        return LIGHT_GREEN
    elif input >=400 and input < 600:
        return GREEN
    elif input >=600 and input < 800:
        return DARK_GREEN

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


    f = open('edgebox1.txt', 'r')
#    num_edgebox1 = f.read()
    col_edgebox1 = define_color(f.read())
    f.close()
    f = open('edgebox1_vm1.txt', 'r')
    col_edgebox1_vm1 = define_color(f.read())
    f.close()
    f = open('edgebox1_vm2.txt', 'r')
    col_edgebox1_vm2 = define_color(f.read())
    f.close()
    f = open('edgebox2.txt', 'r')
    col_edgebox2 = define_color(f.read())
    f.close()
    f = open('edgebox2_vm1.txt', 'r')
    col_edgebox2_vm1 = define_color(f.read())
    f.close()
    f = open('edgebox2_vm2.txt', 'r')
    col_edgebox2_vm2 = define_color(f.read())
    f.close()
    f = open('edgebox2_vm3.txt', 'r')
    col_edgebox2_vm3 = define_color(f.read())
    f.close()
    f = open('kube1.txt', 'r')
    col_kube1 = define_color(f.read())
    f.close()
    f = open('kube2.txt', 'r')
    col_kube2 = define_color(f.read())
    f.close()
    f = open('master.txt','r')
    col_master = define_color(f.read())
    f.close()

    # input source for data - END
    fig = go.Figure(go.Sunburst(
    textfont = {"size":15},
    labels=[" ","K-Fabric","K-Cube1","K-Cube2","K-Cube3","K-Cube4","K-Cube5","eno1","eno2","eno3","eno1  ","eno2  ","eno3  ","eno1 ","eno2 ","eno3 ","eno1   ","eno2   ","eno3   ","eno1    ","eno2    ","eno3    ","vSW1","vSW2","vSW3","VM1","VM2","VM3","vSW1 ","vSW2 ","vSW3 ","VM1 ","VM2 ","VM3 ","     ","  ","   ","    ","      ","       ","c1","c2","c3","c4","c5","c6","d1","d2","d3","d4","d5","d6","e1","e2","e3","e4","e5","e6","f1","f2","f3","f4","f5","f6","g1","g2","g3","g4","g5","g6","h1","h2","h3","h4","h5","h6","i1","i2","i3","i4","i5","i6","j1","j2","j3","j4","j5","j6","k1","k2","k3","k4","k5","k6","l1","l2","l3","l4","l5","l6","m1","m2","m3","m4","m5","m6",],#9
# all the settings below probably follows the order of the labels above

parents=[""," ","K-Fabric","K-Fabric","K-Fabric","K-Fabric","K-Fabric","K-Cube1","K-Cube1","K-Cube1","K-Cube2","K-Cube2","K-Cube2","K-Cube3","K-Cube3","K-Cube3","K-Cube4","K-Cube4","K-Cube4","K-Cube5","K-Cube5","K-Cube5","eno1    ","vSW1","vSW1","vSW3","vSW3","vSW2","eno1","vSW1 ","vSW1 ","vSW3 ","vSW3 ","vSW2 ","eno2","eno3","  ","  ","     ","     ","eno1  ","eno1  ","c1","c1","c2","c2","eno2  ","eno2  ","d1","d1","d2","d2","eno3  ","eno3  ","e1","e1","e2","e2","eno1 ","eno1 ","f1","f1","f2","f2","eno2 ","eno2 ","g1","g1","g2","g2","eno3 ","eno3 ","h1","h1","h2","h2","eno1   ","eno1   ","i1","i1","i2","i2","eno2   ","eno2   ","j1","j1","j2","j2","eno3   ","eno3   ","k1","k1","k2","k2","eno2    ","eno2    ","l1","l1","l2","l2","eno3    ","eno3    ","m1","m1","m2","m2",],
# values = [BPF2, BPF3, BPF1] : BFP1 size doesn't really change

marker = {"colors":[WHITE,WHITE,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,GRAY,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,],
        "line":{'color':[BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,]}}, # in the order of BPF2, BPF3
        
        ))  # set row / col here
#    fig.update_layout(grid=dict(columns=1,rows=1),margin = dict(t=0, l=0, r=0, b=0)) # maybe this is where they change the subplot
    f.close()
    return fig

go.visible = False

app.run_server(debug=True)

#kafka_consumer()
