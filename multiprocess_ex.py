import os
import time

from multiprocessing import Process, Pipe

def doubler():
    number =0
    while True:
        result = number * 2
        proc = os.getpid()
        print('{0} doubled to {1} by procss id : {2}'.format(number,result,proc))
 #       print('\n\n\n ===== yo ===== \n\n\n')
 #       data = q.get()
 #       print('data 1 = {0}, data 2 = {1}'.format(data[0],data[1]))
        time.sleep(5)

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

    proc1 = Process(target=doubler)
#    proc2 = Process(target=test)
    procs = []
    procs.append(proc1)
#    procs.append(proc2)
    proc1.start()
#    proc2.start()

    while True :
        x = input('input x : ')
        y = input('input y : ')
        print('x = {0}, y = {1}'.format(x,y))
        data = [x, y]

    for proc in procs:
        proc.join()


""" 
process input can only be done in main. stdin is shutdown automatically when a new thread is creatd
"""
