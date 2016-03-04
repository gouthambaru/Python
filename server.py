#author   :  Pavani Krishna Goutham Baru(paba6303@colorado.edu)
#name     :  server.py
#purpose  :  To make a server which receives data
#date     :  2015.26.10
#version  :  3.4.3
import socket
import argparse
import re
import sys
import hashlib
parser = argparse.ArgumentParser()
parser.add_argument("port")
#if(len(sys.argv)!=2):
    #print("Enter correct number of arguments")
    #sys.exit()
try:
    args = parser.parse_args()
except SystemExit:
    print("Enter correct number of arguments")
    sys.exit()
try:
    port=int(args.port)
except ValueError:
    print("Enter a integer as port number")
    sys.exit()

size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 10)
data1=[]
try:
    s.bind(('127.0.0.1',port))
    s.listen(5)
    while 1:
        c,address=s.accept()
        data = c.recv(1024)
        #print(data)
        data1=str(data).split('|||')
        #print(data1[0][2:6])
        if((data1[0][2:6])=='FILE'):#checks the data is a FILE or not
            datax = c.recv(4096)
            hash=hashlib.sha256()
            hash.update(datax)#hash value is found
            x=(hash.hexdigest())
            data2=data1[1].replace("'","")
            #print(data2)
            f=open("received"+data2,"wb")
            f.write(datax)#write a value into the file
            f.close
            print("The file"+str(" ")+data2+str(" ")+"is received")
            c.send(x.encode("UTF-8"))
            print("sha value sent")
            #print("the message is",datax)
            c.shutdown
            sys.exit()
        else:
            print("the message is",data.decode("UTF-8"))
            c.shutdown
            sys.exit()
                
except OSError:
        print("the socket is already in use")
        sys.exit()
        