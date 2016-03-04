#!/usr/bin/env python3
#author   :  Pavani Krishna Goutham Baru(paba6303@colorado.edu)
#name     :  cilent.py
#purpose  :  To make a client send data to server over TCP
#date     :  2015.26.10
#version  :  3.4.3
import socket
import argparse
import sys
import os
import hashlib
#if(len(sys.argv)!=4):
    #print("Enter correct number of arguments.")
    #sys.exit()
parser = argparse.ArgumentParser()
parser.add_argument("IP")
parser.add_argument("port")
parser.add_argument("message")
#parser.add_argument("check")
try:
    args = parser.parse_args()
except SystemExit:#checks for the correct number of arguments
    print("Enter correct number of arguments")
    sys.exit()
try:
    socket.inet_aton(sys.argv[1])
    if len(sys.argv[1].split("."))!=4:
        raise socket.error
    k="true"
except socket.error:
    print("Please enter a valid IP address")
    sys.exit()

try:
    port=int(args.port)#checks if the port is an integer value or not
except ValueError:
    print("Enter a integer as port number")
    sys.exit()
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 10)
s.connect((args.IP,port))
hash=hashlib.sha256()
if(not(os.path.isfile(args.message))):
    #print(bytes(args.message,'UTF-8'))
    s.send(bytes(args.message,'UTF-8'))
else:
    s.send(bytes('FILE','UTF-8')+bytes('|||','UTF-8')+bytes(args.message,'UTF-8'))
    f=open(args.message,'rb')
    gh=f.read()
    f.close()
    hash.update(gh)
    x=(hash.hexdigest())
    print("The encoded sha value is",x)
    s.send(gh)
    try:
        datax = s.recv(4096)
        #print(datax)
        data1=datax.decode("UTF-8")
        print("The received sha code is",data1)
        if(data1==x):
            print("file transfer complete")
            
        else:
            print("Sha values mismatch")
    except:
        pass
        print("Sha values mismatch")
    s.shutdown