# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt
 
fig = plt.figure()

class Pos(object):
    Px = 0
    Py = 0
    L1 = 0
    L2 = 0

    def __init__(self,Px_,Py_,L1_,L2_):
        self.Px = Px_
        self.Py = Py_
        self.L1 = L1_
        self.L2 = L2_

    def ik(self,L3,fa2,fa1,fa0):
        L3 = math.sqrt((self.Px*self.Px) + (self.Py*self.Py))
    	fa2 = math.acos(((self.L1*self.L1) + (self.L2*self.L2) - (L3 * L3)) / (2*self.L1*self.L2))
    	th2 = math.pi - fa2
    	fa1 = math.acos(((self.L1*self.L1) + (L3 * L3) - (self.L2*self.L2)) / (2*self.L1*L3))
    	#fa0 = math.atan(self.Py / self.Px)
    	th1 = math.atan2(self.Py , self.Px) - fa1#ポイント
        return th1,th2

    def fk(self,th1, th2):
    	x1 = self.L1 * np.cos(th1)
    	y1 = self.L1 * np.sin(th1)
    	x2 = x1 + self.L2 * np.cos((th1+th2))
    	y2 = y1 + self.L2 * np.sin((th1+th2))
        return x1, y1, x2, y2
    	print(x1)
    	print(x2)
    	print(y1)
    	print(y2)

def plot(x,y):
    plt.text(x1, y1, x1, verticalalignment='bottom',horizontalalignment='right',color='green',fontsize=8)
    plt.text(x1, y1-0.8, y1,verticalalignment='bottom', horizontalalignment='right',color='green', fontsize=8)
    plt.text(x2, y2, x2,verticalalignment='bottom', horizontalalignment='right',color='green', fontsize=8)
    plt.text(x2, y2-0.8, y2, verticalalignment='bottom', horizontalalignment='right',color='green', fontsize=8)
    plt.plot(x,y,"r-")
    plt.show()

if __name__ == '__main__':
    pos = Pos(6.0, 7.5, 10, 10)
    (th1, th2) = pos.ik(pos.Px, pos.Py, pos.L1, pos.L2)
    (x1, y1, x2, y2) = pos.fk(th1, th2)
    x = [0, x1, x2]
    y = [0, y1, y2]
    plot(x,y)

