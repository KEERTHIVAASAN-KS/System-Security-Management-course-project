import os
import subprocess


def modifypermission(file,u,g,o):
    command=subprocess.run(["chmod",file,"u="+u,"g="+g,"o="+o],capture_output=True, text=True)
    print(command.stdout)
def showpermission(file):
    command=subprocess.run(["ls","-l",file],capture_output=True, text=True)
    print(command.stdout)
    



