from include import filemonitor,firewall,fileaccess,netscan

while True:
    print("1-SCAN NETWORK VULNERABILITIES\n2-FILE ACCESS CONTROL\n3-CONFIGURE FIREWALL\n4-FILE  MONITORING\n5-EXIT")

    choice=int(input("enter choice:"))
    if choice==1:
        ip=input("enter ip:")
        print("1-PORTSCAN\n2-OSSCAN")
        ch=int(input("enter choice:"))
        if ch==1:
            netscan.portscan(ip)
        elif ch==2:
            netscan.osscan(ip)
        
    elif choice==2:
        file=input("enter file:")
        ch=int(input("1-VIEW PERMISSIONS\n2-MODIFY PERMISSIONS\nenter choice:"))
        if ch==1:
            fileaccess.showpermission(file)
        elif ch==2:
            u=input("enter owner permissions:")
            g=input("enter group permissions:")
            o=input("enter others permissions:")
            fileaccess.modifypermission(file,u,g,o)
        
    elif choice==3:
        print("1-ENABLE\n2-DISABLE\n3-RESET\n4-ADD RULE\n5-VIEW RULES\n6-DELETE RULES")
        ch=int(input("enter choice:"))
        if ch==1:
            firewall.firewallenable()
        elif ch==2:
            firewall.firewalldisable()
        elif ch==3:
            firewall.reset()
        elif ch==4:
            ip=input("enter ip:")
            port=input("enter port:")
            direc=input("inbound/outbound(i/o):")
            if len(ip)!=0 and len(port)==0:
                firewall.addrule(ip,None,direc)
            elif len(ip)==0 and len(port)!=0:
                firewall.addrule(None,int(port),direc)
            else:
                firewall.addrule(ip,int(port),direc)
            
        elif ch==5:
            firewall.viewrules()
        elif ch==6:
            n=int(input("enter rule number:"))
            firewall.deleterule(n)
        
        
    elif choice==4:
        print("1-MONITOR FILES\n2-VIEW LOG")
        ch=int(input("enter choice:"))
        if ch==1:
            files=input("enter files(comma seperated):")
            files=list(files)
            filemonitor.monitor(files)
        
        elif ch==2:
            filemonitor.viewlog()
            
    elif choice==5:
        print("EXITTING...")
        break
        
         
    
        
        
        

