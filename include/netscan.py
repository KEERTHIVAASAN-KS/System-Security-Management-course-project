import nmap


def portscan(targetip):
    scanner=nmap.PortScanner()
    try:
        scanner.scan(targetip,arguments="")
        for i in scanner.all_hosts():
            if scanner[i].state()=="up":
                print("host:",scanner[i]["addresses"]["ipv4"],"is up")
                if "tcp" in scanner[i]:
                    for port in scanner[i]["tcp"]:
                        print("tcp port ",port," ",scanner[i]["tcp"][port]["state"])
                elif "udp" in scanner[i]:
                    for port in scanner[i]["udp"]:
                        print("udp port ",port," ",scanner[i]["udp"][port]["state"])
                
                
                
            else:
                print("host:",targetip," down")
            
    except nmap.PortScannerError:
        print("nmap error")
        
def osscan(targetip):
    scanner=nmap.PortScanner()
    try:
        scanner.scan(targetip,arguments="-O")
        for i in scanner.all_hosts():
            if scanner[i].state()=="up":
                print("host:",scanner[i]["addresses"]["ipv4"],"is up")
                if "tcp" in scanner[i]:
                    for port in scanner[i]["tcp"]:
                        print("tcp port ",port," ",scanner[i]["tcp"][port]["state"])
                elif "udp" in scanner[i]:
                    for port in scanner[i]["udp"]:
                        print("udp port ",port," ",scanner[i]["udp"][port]["state"])
                if "osmatch" in scanner[i]:
                    for os in scanner[i]["osmatch"]:
                        print(os["name"],"accuracy:",os["accuracy"])
                  
            else:
                print("host:",targetip," down")
            
    except nmap.PortScannerError:
        print("nmap error")
    
    
    
    

