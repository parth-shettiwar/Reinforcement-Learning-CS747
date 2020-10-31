import sys
import numpy as np
loc  = sys.argv[2]
ff = np.loadtxt(loc)
loc2  = sys.argv[4]
flag=1
path = []
prev = []
ss = np.where(ff==2)
start_co = [ss[0][0],ss[1][0]]
en = np.where(ff==3)
end_co = []
for i in range(len(en[0])):

    end_co.append([en[0][i],en[1][i]])

curr = start_co
f = open(loc2, "r")
Lines = f.readlines()

dec = np.zeros((ff.shape[0]*ff.shape[1]))
for i in range(len(Lines)):
    dec[i] = Lines[i].split()[1]

dec = dec.reshape((ff.shape[0],ff.shape[1]))

dic = {0:"W",1:"E",2:"N",3:"S"}
while(flag==1):
    
    act = dec[curr[0],curr[1]]
    path.append(dic[act])
    if(act==0):
        curr = [curr[0],curr[1]-1]
        
        
    if(act==1):
        curr = [curr[0],curr[1]+1]
             
    if(act==2):
        curr = [curr[0]-1,curr[1]]
                
    if(act==3):
        curr = [curr[0]+1,curr[1]]

    for i in range(len(end_co)):
        if(end_co[i]==curr):

            flag=0 
print(*path)