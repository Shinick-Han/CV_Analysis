import pandas as pd
from pandas import DataFrame
import numpy as np
import os
import matplotlib.pyplot as plt
import tkinter, tkfilebrowser
from numpy import loadtxt

def selectplot(files,inx,iny):
    with open(files) as f:
        list_of_lists = []
        for line in f:
            inner_list = [elt.strip() for elt in line.split()]
            list_of_lists.append(inner_list)
        by_cols = zip(*list_of_lists)
        listss = DataFrame(list_of_lists)
        columns1 =[]
        column_size = 0
        while column_size < listss.shape[1]:
            columns1.append(str(column_size))
            column_size = column_size + 1
        listss.columns = columns1
        types = 0
        while listss['0'][types] != str("datasets"):
            types += 1
        typee = 0
        while listss['0'][typee] != str("functions"):
            typee += 1
        datas = 0
        while listss['0'][datas] != str("Data"):
            datas += 1
        endofline = 0
        while listss[str(int(endofline))][typee-1] != str("]"):
            endofline += 1
        v = 0
        w = 0
        t = []
        while w < typee-types-3:
            v = 0
            while v < listss.shape[1]-1:
                t.append(str(listss[str(int(v))][types+w+2]))
                v = v + 1
            w = w + 1
        v = 0
        while v < endofline:
            t.append(str(listss[str(int(v))][typee-1]))
            v += 1
        print(t)
        v = np.full((1,len(t)),0)
        w = 0
        while w < len(t):
            v[0][w] = w
            w = w + 1
        print(v[0])

def openplot(files,inx,iny):
    with open(files) as f:
        list_of_lists = []
        for line in f:
            inner_list = [elt.strip() for elt in line.split()]
            list_of_lists.append(inner_list)
        by_cols = zip(*list_of_lists)
        listss = DataFrame(list_of_lists)
        columns1 =[]
        column_size = 0
        while column_size < listss.shape[1]:
            columns1.append(str(column_size))
            column_size = column_size + 1
        listss.columns = columns1
        types = 0
        while listss['0'][types] != str("datasets"):
            types += 1
        typee = 0
        while listss['0'][typee] != str("functions"):
            typee += 1
        datas = 0
        while listss['0'][datas] != str("Data"):
            datas += 1
        endofline = 0
        while listss[str(int(endofline))][typee-1] != str("]"):
            endofline += 1
        v = 0
        w = 0
        t = []
        while w < typee-types-3:
            v = 0
            while v < listss.shape[1]-1:
                t.append(str(listss[str(int(v))][types+w+2]))
                v = v + 1
            w = w + 1
        v = 0
        while v < endofline:
            t.append(str(listss[str(int(v))][typee-1]))
            v += 1
    voltage = np.full(((int((listss.shape[0]-datas-typee+types-1)/int(typee-types-1))), 1), 0.00000000000000000000000)
    capacitance = np.full(((int((listss.shape[0]-datas-typee+types-1)/(typee-types-1))), 1), 0.00000000000000000000000)
    i = 0
    j = int(datas + 2 + int(inx/5))     ## datas + share + 2
    k = int(datas + 2 + int(iny/5))     ## datas + share + 2
    while i < int(int(listss.shape[0]-datas-typee+types-1)/int(typee-types-1)):
        voltage[int(i)] = float(listss[str(int(inx%5))][j + i * 3])
        capacitance[int(i)] = float(listss[str(int(iny % 5))][k + i * 3])
        i = i + 1
    s = str(files)
    plt.plot(voltage, capacitance, label = s.replace('C:\\Users\\DCLAB\\Desktop\\신익\\200526_sim_result\\200526_sim_result\\CV_Dit_Freq_wResult\\200525_CV_Dit_Freq\\',''))
    plt.xlabel(str(listss[str(int(inx%5))][int(types+2+int(inx/5))]))
    plt.ylabel(str(listss[str(int(iny%5))][int(types+2+int(iny/5))]))
files = tkfilebrowser.askopenfilenames()
# files might be "file1.txt file2.exe file3.bmp" at this point
a = len(files)
c = 0
inx = 0
iny = 0
########################## CV Plotting ####################################
selectplot(files[c],inx,iny)
print("X축")
inx = int(input())
print("Y축")
iny = int(input())
while c < a:
    openplot(files[c],inx,iny)
    c = c + 1
plt.legend()
plt.show()

