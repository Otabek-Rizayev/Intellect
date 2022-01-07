import sys
import os
import time
from register import registration

clear = os.system('cls')

#class commands:
    #def __init__(self, comm, comm2, reg):
       # self.comm = comm
        #self.comm2 = comm2
        #self.reg = reg
        
def dialog():
    print("Hacker")

def comm2():
    clear()
    print("Tozalandi!")
    time.sleep(0.5)
    clear()
        
def reg():
    import register
    
while True:
    intellect = input(">>> ")
    if intellect == 'clear':
        print(comm2())
    elif intellect == 'registration':
        print(registration())
    else:
        continue
    print(f">> {intellect} komandasi xato kiritildi!")
    
