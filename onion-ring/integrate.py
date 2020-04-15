import os
import subprocess
from pymongo import MongoClient
import time
import plotly.graph_objects as go
import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


IP_EDGEBOX1 = '172.30.84.93'
IP_EDGEBOX2 = '172.30.84.92'
IP_KUBE1 = '172.30.84.95'
IP_KUBE2 = '172.30.84.94'
IP_MASTER = '172.30.84.96'
IP_EDGEBOX2_VM1 = '192.168.122.205'
IP_EDGEBOX2_VM2 = '192.168.122.134'
IP_EDGEBOX2_VM3 = '192.168.122.142'
IP_EDGEBOX1_VM1 = '192.168.122.178'
IP_EDGEBOX1_VM2 = '192.168.122.173'

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

col_edgebox1 = YELLOW
col_edgebox2 = YELLOW
col_kube1 = YELLOW
col_kube2 = YELLOW
col_master = YELLOW
col_edgebox2_vm1 = YELLOW
col_edgebox2_vm2 = YELLOW
col_edgebox2_vm3 = YELLOW
col_edgebox1_vm1 = YELLOW
col_edgebox1_vm2 = YELLOW

# connecting to pymongo db

PKT_THRESHOLD = 10

client = MongoClient('localhost',27017)
db = client['packetmonitor']
collection = db['bpf2']

result = 0

def print_value():
        num_edgebox1 = 0
        num_edgebox2 = 0
        num_kube1 = 0
        num_kube2 = 0
        num_master = 0
        num_edgebox2_vm1 = 0
        num_edgebox2_vm2 = 0
        num_edgebox2_vm3 = 0
        num_edgebox1_vm1 = 0
        num_edgebox1_vm2 = 0

        current_time = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]).zfill(2)

        current_time_minus_5 = str(time.localtime()[0]) + ';' + str(time.localtime()[1]).zfill(2) + ';' + str(time.localtime()[2]).zfill(2) + ';' + str(time.localtime()[3]).zfill(2) + ';' + str(time.localtime()[4]).zfill(2) + ';' + str(time.localtime()[5]-5).zfill(2)
        global result
 
        for post in collection.find({'time':{'$gt':current_time_minus_5,'$lt':current_time}},{'_id':0,'dst_ip':1,'pkt_num':1}):
            print(post)
            pos_start = str(post).find('u\'dst_ip\': ') + 13
            pos_end = str(post).find(', u\'pkt_num\':') -1
            temp_ip = str(post)[pos_start:pos_end]

            counter = 0
            temp = str(post)[::-1]
            for i in temp:
                if i == ':':
                    break
                else:
                    counter = counter+1

            temp_pkt_num = int(str(post)[-counter+3:-2])
            print(temp_ip)
            if (temp_ip == IP_EDGEBOX1):
                num_edgebox1 = num_edgebox1 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2):
                num_edgebox2 = num_edgebox2 + temp_pkt_num
            elif (temp_ip == IP_KUBE1):
                num_kube1 = num_kube1 + temp_pkt_num
            elif (temp_ip == IP_KUBE2):
                num_kube2 = num_kube2 + temp_pkt_num
            elif (temp_ip == IP_MASTER):
                num_master = num_master + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2_VM1):
                num_edgebox2_vm1 = num_edgebox2_vm1 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2_VM2):
                num_edgebox2_vm2 = num_edgebox2_vm2 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX2_VM3):
                num_edgebox2_vm3 = num_edgebox2_vm3 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX1_VM1):
                num_edgebox1_vm1 = num_edgebox1_vm1 + temp_pkt_num
            elif (temp_ip == IP_EDGEBOX1_VM2):
                num_edgebox1_vm2 = num_edgebox1_vm2 + temp_pkt_num

        print("edgebox1 " + str(num_edgebox1))
        print("edgebox2 " + str(num_edgebox2))
        print("kube1 " + str(num_kube1))
        print("kube2 " + str(num_kube2))
        print("master " + str(num_master))
        print("edgebox2_vm1 " + str(num_edgebox2_vm1))
        print("edgebox2_vm2 " + str(num_edgebox2_vm2))
        print("edgebox2_vm3 " + str(num_edgebox2_vm3))
        print("edgebox1_vm1 " + str(num_edgebox1_vm1))
        print("edgebox1_vm2 " + str(num_edgebox1_vm2))

#        print(post)
#        result = result + int(str(post)[15:-2])

# to write a system command, refer to the line below:
#subprocess.call(["apt-get","update"])
#subprocess.checkoutput(

# remove the annotation block and integratre this code later 
# save black_list map id - begin
'''
num = entire_bpf_map_info.find("black_list")
test = num - 30
test2 = entire_bpf_map_info[test:num]
num2 = test2.find('\n')
test3 = test2[num2:]
num3 = test3.find(':')
test4 = test3[:num3]
black_list_map_id = int(test4)
print('- targetted bpf map id : ' + str(test4))
'''
#save black_list map id - end

# update bpf map value - begin
#subprocess.call(["bpftool","map","update","id",str(black_list_map_id),"key","00","00","00","00","value","01","00","00","00","00","00","00","00"])
# update bpf map value - end


ip_address = []
pkt_num = []

def add_to_ip_saver(addr_merged, num):
    global ip_address
    global pkt_num

    if (addr_merged in ip_address):        # when returns True
        index = ip_address.index(addr_merged)
        pkt_num[index] = str(int(pkt_num[index]) + int(num))
    elif (not addr_merged in ip_address):  # when returns False
        ip_address.append(addr_merged)
        pkt_num.append(num)

#copy - begin
        
mid_val3 = [0,0,0]

# define colors codes here
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

    marker = {"colors":[temp_color,col_master,col_kube1,col_kube2,col_edgebox1,col_edgebox2,col_edgebox2_vm1,col_edgebox2_vm2,col_edgebox2_vm3,col_edgebox1_vm1,col_edgebox1_vm2,WHITE,WHITE,WHITE],
        "line":{'color':[BLACK]}}, # in the order of BPF2, BPF3
        ))  # set row / col here
#    fig.update_layout(grid=dict(columns=1,rows=1),margin = dict(t=0, l=0, r=0, b=0)) # maybe this is where they change the subplot
    f.close()
    return fig

# copy - end

go.visible = False

app.run_server(debug=True)

#kafka_consumer()
        

try:
    while True:
        print_value()
        time.sleep(1)
except KeyboardInterrupt:
    pass
