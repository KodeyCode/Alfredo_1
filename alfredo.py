from sys import argv,exit
from os import system
import platform
import importlib
import requests
from datetime import datetime

global f
#Variables
try:
    f = open(argv[1])
except:
    print('\u001b[31mError: the file "'+argv[1]+'" was not found.')
    exit()
vars = {"version":"1.0","time":"","date":"","filename":"","os":""}
now = datetime.now()
os = platform.system()

#Interpreter loop
for line in f:
    vars.update({"time":now.strftime("%H:%M")})
    vars.update({"date":now.strftime('%d/%m/%Y')})
    vars.update({"version":"1.0"})
    vars.update({"filename":f.name})
    vars.update({"os":os})
    tokens = line.split(':')
    if tokens[0] == 'out':
        if tokens[1] == 'var':
            try:
               print(vars[tokens[2]])
            except:
                print('\u001b[31mError: "'+tokens[2]+'" is not a variable')
        else:
            print(tokens[1])
    elif tokens[0] == 'var':
        if tokens[1] == '/in/':
            var = input()
            vars.update({tokens[2]:var})
        else:
            vars.update({tokens[2]:tokens[1]})
    elif tokens[0] == 'file':
        if tokens[1] == 'write':
            try:
                f2 = open(tokens[2],"w")
                f2.write(tokens[3])    
            except:
                print('\u001b[31mError: the file "'+tokens[2]+'" was not accessible.')
        if tokens[1] == 'append':
            try:
                f2 = open(tokens[2],"a")
                f2.write(tokens[3])    
            except:
                print('\u001b[31mError: the file "'+tokens[2]+'" was not accessible.')
        if tokens[1] == 'read':
            try:
                f2 = open(tokens[2],"r")
                read = f2.read()
                print(read)
            except:
                print('\u001b[31mError: the file "'+tokens[2]+'" was not accessible.')
        if tokens[1] == 'varto':
            f2 = open(tokens[3],"r")
            read = f2.read()
            vars.update({tokens[2]:read})
    elif tokens[0] == 'shell':
        try:
            system(tokens[1])
        except:
            print('\u001b[31mError: "'+tokens[1]+'" was not identified as a command.')
    elif tokens[0] == 'clr':
        if os == "windows":
            system('cls')
        if os == "linux" or "unix":
            system('clear')