import os
import subprocess


def firewallenable():
    command=subprocess.run(["ufw","enable"],capture_output=True, text=True)
    print(command.stdout)

def addrule(ip,port,direction):
    if direction=="i":
        if ip is None:
            command=subprocess.run(["ufw","deny",str(port)],capture_output=True, text=True)      
            print(command.stdout)
        elif port is None:
            
            command=subprocess.run(["ufw","deny","from",ip],capture_output=True, text=True)
            print(command.stdout)

        else:
            command=subprocess.run(["ufw","deny","from",ip,"to","any","port",str(port)],capture_output=True, text=True)
            print(command.stdout)
 
    if direction=="o":
        if ip is None:
            command=subprocess.run(["ufw","deny","out",str(port)],capture_output=True, text=True)
            print(command.stdout)
 
        elif port is None:
            command=subprocess.run(["ufw","deny","out","to",str(port)],capture_output=True, text=True)
            print(command.stdout)
 
        else:
            command="ufw deny out to "+ip+" port "+str(port)
            command=subprocess.run(["ufw","deny","out","to",ip,"port",str(port)],capture_output=True, text=True)
            print(command.stdout)
            
           
def viewrules():
    command=subprocess.run(["ufw","status","numbered"],capture_output=True, text=True)
    print(command.stdout)
def deleterule(number):
    command=subprocess.run(["ufw","delete",str(number)],capture_output=True, text=True)
    print(command.stdout)
 
def reset():
    command=subprocess.run(["ufw","reset"],capture_output=True, text=True)
    print(command.stdout)
 
def firewalldisable():
    command=subprocess.run(["ufw","disable"],capture_output=True, text=True)
    print(command.stdout)
    
    
 
    
