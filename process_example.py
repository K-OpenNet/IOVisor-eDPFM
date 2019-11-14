import os
import time

from multiprocessing import Process, Pipe

def doubler(conn):
    number =0
    testo = 0
    while testo != -1:
        testo = conn.recv()
        result = number * 2
        proc = os.getpid()
        print('{0} doubled to {1} by {2} '.format(proc,number,conn.recv()))
        time.sleep(5)
    conn.close()

def test():
   """
    while True:
        x = raw_input("input x : ")
        y = raw_input("input y : ")
        print('x = {0}, y = {1}'.format(x,y))

    x = input('input x : ')
    y = input('input y : ')
    """

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    proc1 = Process(target=doubler,args=(child_conn,))
#    proc2 = Process(target=test)
    procs = []
    procs.append(proc1)
#    procs.append(proc2)
    proc1.start()
#    proc2.start()
    x=0
    while x != -1 :
        x = input('input x : ')
        parent_conn.send(x)
        
        
    for proc in procs:
        proc.join()


""" 
process input can only be done in main. stdin is shutdown automatically when a new thread is creatd
"""
