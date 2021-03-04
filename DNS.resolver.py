#!/usr/bin/env python3
#author   :  Pavani Krishna Goutham Baru(paba6303@colorado.edu)
#name     :  file3.py
#purpose  :  To make a DNS resolver
#date     :  2015.19.10
#version  :  3.4.3
import socket
import sys
if(len(sys.argv)!=2):
    print("Please enter correct number of arguments")
    sys.exit()
gh=[]
gh=sys.argv[1].split('.')
try:
    l=int(gh[0])
    k="True"
except ValueError:
    k="False"
if(k=="True"):
    ip=sys.argv[1]
    try:
        socket.inet_aton(sys.argv[1])
        if len(sys.argv[1].split("."))!=4:
            raise socket.error
        k="True"
        #print("dance")
    except socket.error:
        print("Please enter a valid IP address")
        k="False"
        sys.exit()
    try:
        print("The host name of the ip is",socket.gethostbyaddr(ip)[0])
        sys.exit()
    except socket.herror:
        print("NO host with that IP adress")
        sys.exit()
elif(k=="False"):
    name=sys.argv[1]
    try:
        print("The ip address of the host is",socket.gethostbyname(name))
    except socket.gaierror:
        print("No domainname exists with that name")
        sys.exit()
else:
    print("Not found")