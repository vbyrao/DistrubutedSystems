from xmlrpc.client import ServerProxy
from pathlib import Path
import os

LOCAL_DIRNAME = "./client_files/"
SERVER_ADDRESS = "http://localhost:8000"

with ServerProxy(SERVER_ADDRESS) as server:
    while 1:
        print("Enter word of choice\n")
        print("upload\n")
        print("download\n")
        print("rename\n")
        print("delete\n")
        print("add\n")
        print("sort\n")
        
        choice = input()
        if(choice=="upload"):
            fname = input()
            f = open("./client_files/"+fname)
            server.upload(fname,f.read())
            f.close()
        if(choice=="download"):
            fname = input()
            content = server.download(fname).data
            Path(os.path.join("./client_files/", fname)).write_bytes(content)
            print("downloded")
        if(choice=="rename"):
            old_name = input()
            new_name = input()
            try:
                server.rename(old_name,new_name)
            except:
                print()
        if(choice=="delete"):
            fname = input()
            server.delete(fname)
        if(choice=="add"):
            print("Enter a")
            a = int(input())
            print("Enter b")
            b = int(input())
            print(server.add(a,b))
        if(choice=="sort"):
            a = list(map(int,input().split()))
            r = server.sort(a)
            print(r)
            