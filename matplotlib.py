#!/usr/bin/env python3
#author   :  Pavani Krishna Goutham Baru(paba6303@colorado.edu)
#name     :  file1client.py
#purpose  :  To ping two servers and plot the RTTs 
#date     :  2015.9.11
#version  :  3.4.3
import matplotlib.pyplot as plt
import subprocess
import csv
import re
import sys
from prettytable import PrettyTable
if(len(sys.argv)>2):
    print ("enter correct number of arguments")
    sys.exit()
table=PrettyTable(["ping count","ping to 8.8.8.8(ms)"])
table1=PrettyTable(["ping count","ping to 4.2.2.1(ms)"])
table2=PrettyTable(["ping count","ping to 8.8.8.8(ms)","ping to 4.2.2.1(ms)"])
counter=0
counter1=0
x=[]
y=[]
z=[]
a=[]
ve=[]
ve1=[]
try: 
    for i in range(0,50):
        #print(i)
        s = subprocess.Popen(["ping","-n","1","8.8.8.8"],stdout=subprocess.PIPE).stdout.read()
        person= re.findall(r'Average = \d+\ms',str(s))
        #print(person)
        if(len(person) is 0):
            counter=counter+1
            ve.append("NO response from the server")
            #print(counter)
            if(counter==5):
                n=i;
                
                raise StopIteration
            
        elif(counter<6):
            
            x=(str(person).split('='))
            y=x[1].split('ms')
            #print(y[0])
            z.append(int(y[0]))
            ve.append(int(y[0]))
            #print(i)
            
except StopIteration:
    #if(n>6):
        #print(table)
    for nat in range(n,49):
        ve.append("ping attempt terminated after"+str(n)+"trials")
    #print(len(ve))
        
    
    pass
try:
    for i in range(0,50):
        s = subprocess.Popen(["ping","-n","1","4.2.2.1"],stdout=subprocess.PIPE).stdout.read()
       
        person= re.findall(r'Average = \d+\ms',str(s))
        if(len(person) is 0):
            counter1=counter1+1
            ve1.append("NO response from the server")
            #print(counter1)
            if(counter1==5):
                j=i;
                raise StopIteration
        elif(counter1<6):
            x=(str(person).split('='))
            y=x[1].split('ms')
            #print(y[0])
            a.append(int(y[0]))
            #print(len(a))
            ve1.append(y[0])
            
except StopIteration:
    #if(j>5):
        #print(table1)
    for nat in range(j,49):
        ve1.append("ping attempt terminated after"+str(j)+" "+"trials")
    #print(len(ve))
    
    pass
for i in range(0,50):
    table2.add_row([i,ve[i],ve1[i]])
print(table2)
plt.plot(z,color='black')
plt.plot(a,color='red')
plt.legend(['8.8.8.8','4.2.2.1'],loc='upper left')
plt.ylabel("Time in ms")
plt.xlabel("Ping count")
plt.title("Ping values for different servers")
if(len(a)==0 and len(z)==0):
    print("Both the servers didnot respond")
    sys.exit()
elif(len(a)==0):
    plt.ylim([0,(max(z))+40])
    plt.xlim([0,49])
elif(len(z)==0):
    plt.ylim([0,(max(a))+40])
    plt.xlim([0,49])
else:
    plt.ylim([0,max(max(z),max(a))+40])
    plt.xlim([0,49])
if(len(sys.argv)==2):
    try:
        plt.savefig(sys.argv[1]+".png")
    except ValueError:
        print("Please save in supported format:jpeg,png,tiff")
plt.show()
