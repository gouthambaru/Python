#!/usr/bin/env python3
#author   :  Pavani Krishna Goutham Baru(paba6303@colorado.edu)
#name     :  file1.py
#purpose  :  To make use of tkinter and create a GUI with 3 buttons
#date     :  2015.15.11
#version  :  3.4.3
import sys
try:#checking whether the module Tkinter is installed or not
    from Tkinter import *
except ImportError:
    print("the module tkinter is not installed ")
    sys.exit()
import socket
import urllib2
try:
    import requests
except ImportError:#checking whether the module requests is installed or not
    print("the module requests is not installed ")
    sys.exit()
try:
    from bs4 import BeautifulSoup#checking whether the module BeautifulSoup is installed or not
except ImportError:
    print("the module BeautifulSoup is not installed ")
    sys.exit()

def endWindow():#Function for closing the window
    root.destroy()
    
root=Tk()
root.geometry('320x340')#defining the window size
def readButton(x):#Check the Button 
    print("Button"+x+"pressed")
Label(root,text="Homework 10").grid(row=1,column=1,columnspan=3,ipadx="110")#Defining the title of the box
display=Label(root,text="")
display.grid(row=3,column=1,columnspan=3)
def lookup():#Defining a function for resolving a hostname
    ipaddr=socket.gethostbyname("www.colorado.edu")
    #print(ipaddr)
    display.configure(text="the IP address of colorado.edu is " + ipaddr)
def title():#Function for extracting a title
    try:
        requests.get("https://www.colorado.edu")
    except requests.exceptions.ConnectionError:#Checking whether the Internet connection exists
        print("No Domain name exists with that name")
        display.configure(text="No Domain name exists with that name")
        sys.exit()
    except requests.exceptions.MissingSchema:#Checking whether the URL exists or not
        print("Invalid URL")
        print("Might be missing http")
        display.configure(text="Invalid URL:Might be missing http")
        sys.exit()
    soup=BeautifulSoup(urllib2.urlopen("https://www.colorado.edu"),"html.parser")
    #print(soup.title.string)
    display.configure(text=soup.title.string)
buttonA=Button(root,text="hostnameresolver",command=lambda: lookup()).grid(row=2,column=1)#Defining the buttons in their respective positions
buttonB=Button(root,text= "Title",command=lambda: title()).grid(row=2,column=2)
buttonC=Button(root,text= "EndProgram",command=lambda: endWindow()).grid(row=2,column=3)
root.mainloop()