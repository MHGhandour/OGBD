# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 15:48:45 2018

@author: mhg
"""
from __future__ import division,print_function
import numpy as np
import threading
import time

class SUMThread(threading.Thread):         
    def summ(a):
        a[0,1]=2*a[0]+1
        return(a)
    def run(self):
        print("{} started!".format(self.getName()))
        print("{} finished!".format(self.getName())) 
a=np.array([[1,1],[2,2],[3,3],[4,4]])        
if __name__ == '__main__':
    for x in range(4):                                        
        mythread = SUMThread.summ(a[x])
        mythread.start()                                      
        time.sleep(.9)  