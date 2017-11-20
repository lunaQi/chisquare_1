# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import os
f1 = open("/Users/luna/nudoc/car/car.txt", 'r')
lines = f1.readline()   #readlines自动将文件内容存到一个行的列表
attribute_dic = {}
for word in lines:
    attribute_dic[word] = {}
'''''
path = "/Users/luna/af_stopwords/training-car"
#path = "/Users/luna/PycharmProjects/CHI/training_test/car"
#os.makedirs("/Users/luna/nudoc/car")
#nudoc_path = "/Users/luna/nudoc/car"
files = os.listdir(path)
file_path = []
for file in files:
    child = os.path.join('%s/%s' %(path,file))
    if('.DS_Store' not in child):
        file_path.append(child)
for file in file_path:
    f_o2o = open(file, 'r')
    words = f_o2o.readlines()
    text_set = set(words)
    
'''
#data = pd.read_table(attribute_dic)

#print data
