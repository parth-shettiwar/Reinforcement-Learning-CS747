import numpy as np
import sys

loc  = sys.argv[2]
ff = np.loadtxt(loc)
Num_States = ff.shape[0]*ff.shape[1]
H = ff.shape[0]
B = ff.shape[1]
Trans = np.zeros((Num_States,4,Num_States))
Rew = np.ones((Num_States,4,Num_States))
coun = 0
end = []
for i in range(H):
    for j in range(B):
        if(ff[i][j]==3):
            end.append(i*B + j)
        if(ff[i][j]==2):
           start = i*B + j   
           start_co = [i,j]  
        coun += 1  
eps = 0.0000000000001  
rew_cos = 1 
  
for i in range(H):
    for j in range(B):
        if(ff[i][j]!=1): 
            if(j-1>=0):
                Trans[i*B + j][0][i*B + j-1] = 1
                Rew[i*B + j][0][i*B + j-1] = -100*(ff[i][j-1]==1)
            if(j+1<B):
                Trans[i*B + j][1][i*B + j+1] = 1
                Rew[i*B + j][1][i*B + j+1] = -100*(ff[i][j+1]==1)
            if(i-1>=0):
                Trans[i*B + j][2][(i-1)*B + j] = 1
                Rew[i*B + j][2][(i-1)*B + j] = -100*(ff[i-1][j]==1)
            if(i+1<H):
                Trans[i*B + j][3][(i+1)*B + j] = 1
                Rew[i*B + j][3][(i+1)*B + j] = -100*(ff[i+1][j]==1)                                    

for i in range(len(end)):
    Rew[:,:,end[i]] = 100
 
for i in range(len(end)):

    Trans[end[i],:,:] = 0

Num_Actions = 4
gamma = .9

print("numStates",Num_States)
print("numActions",Num_Actions)
print("start",start)
print("end",*end)
for s in range(0, Num_States):
    for a in range(0, Num_Actions):
     
        for i in range(Num_States):
            if(Trans[s,a,i]!=0):
                print("transition",s,a,i,Rew[s][a][i],Trans[s][a][i])
            
print("mdptype","episodic")
print("discount ",gamma)






        
