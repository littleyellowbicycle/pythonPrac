# -- coding: utf-8 --
from sys import argv 
import os

script,first=argv

cwd=os.getcwd()
res=os.listdir(cwd)
#-a
def print_all(res):
    for string in res:
        print string+'\t',
    print '.'+'\t'+'..'+'\t'
#-A
def print_all_without_default(res):
    for string in res:
        #if string!='.'and string!='..':
        print string+'\t'
#-B
def print_all_without_simple(res):
    for string in res:
        if string[-1]!='~'and string[-1]!='~':
            print string+'\t',
#-c
def print_all_sort(res):
    dict = {}
    for str in res:
        ctime=os.path.getctime(str)
        dict[str]=ctime
    dic_ctime=sorted(dict.items(),key=lambda item:item[1])
    for item in dic_ctime:
        print item[0]+'\t'
    #print dic_ctime.keys()

if first=='a':
    print_all(res)
elif first=='A':
    print_all_without_default(res)
#elif first=='b':
#    print_all_with_simple(res)
elif first=='B':
    print_all_without_simple(res)
elif first=='c':
    print_all_sort(res)
else:
    print "lol"
#elif first=='C':
#elif first=='D':
#elif first=='d':
#elif first=='f':
#elif first=='F':

