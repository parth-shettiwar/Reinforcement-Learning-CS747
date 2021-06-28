import numpy as np

import sys 
import pulp as pl

def vi(Num_States,Num_Actions,Trans,Rew, gamma):

    New_Val = np.ones((Num_States))
    coun = 0
    Policy = np.zeros((Num_States))
    Value = np.zeros((Num_States))

    while((abs(New_Val-Value)>1e-12).any()):
        
        if(coun>0):
            Value =  New_Val.copy()            
        
        New_Val= np.max(np.sum(Trans*(Rew+gamma*Value*np.ones((Num_States,Num_Actions,Num_States))),axis = 2),axis = 1)
        Policy = np.argmax(np.sum(Trans*(Rew+gamma*Value*np.ones((Num_States,Num_Actions,Num_States))),axis = 2),axis = 1)
        coun += 1    

    return Policy, New_Val

def hpi(Num_States,Num_Actions,Trans,Rew, gamma):
    Impr = np.zeros((Num_States,Num_Actions))
    Q_val = np.zeros((Num_States,Num_Actions))
    Policy = np.zeros((Num_States),dtype = np.int)

    flag = 1    
    while(flag==1): 
        flag=0   
        prob = pl.LpProblem("myProblem", pl.LpMinimize)



        Val = pl.LpVariable.dicts("val", range(Num_States),cat=pl.LpContinuous)
        for i in range(Num_States):
            prob += Val[i] == pl.lpSum([Trans[i][Policy[i]][j]*(Rew[i][Policy[i]][j]+gamma*Val[j])  for j in range(Num_States)])
        prob.solve(pl.PULP_CBC_CMD(msg=0))

        for i in range(Num_States):
            for j in range(Num_Actions):
            
                sum_temp = 0
                sum_temp2 = 0
                for z in range(Num_States):
                    sum_temp += Trans[i][j][z]*(Rew[i][j][z]+gamma*pl.value(Val[z]))
                Q_val[i][j] = sum_temp
            temp = np.argmax(Q_val[i]) 
            if(Q_val[i][temp] > Q_val[i][Policy[i]]):
             
                flag=1
                Policy[i]  = temp  
    value = np.zeros((Num_States))            
    for i in range(Num_States):
        value[i] = pl.value(Val[i])            
    return Policy, value
     

def lp(Num_States,Num_Actions,Trans,Rew, gamma):
    prob = pl.LpProblem("myProblem", pl.LpMinimize)
    
    
    Val = pl.LpVariable.dicts("val", range(Num_States),cat=pl.LpContinuous)
    prob += pl.lpSum(Val[j] for j in range(Num_States))
    for i in range(Num_States):
        for k in range(Num_Actions):
            prob += Val[i] >= pl.lpSum([Trans[i][k][j]*(Rew[i][k][j]+gamma*Val[j])  for j in range(Num_States)])
    prob.solve(pl.PULP_CBC_CMD(msg=0))
    value=np.zeros((Num_States))
    for i in range(Num_States):
        value[i]=pl.value(Val[i])    
    Policy = np.argmax(np.sum(Trans*(Rew+gamma*value*np.ones((Num_States,Num_Actions,Num_States))),axis = 2),axis = 1)

    return Policy, value
cc = len(sys.argv)
if(cc>2):
    loc  = sys.argv[2]
    algorithm =  sys.argv[4]
f = open(loc, "r")
Lines = f.readlines()
Num_States = int(Lines[0].split()[1])
Num_Actions = int(Lines[1].split()[1])
Trans = np.zeros((Num_States,Num_Actions,Num_States))
end = []
ee = Lines[3].split()

task = Lines[len(Lines)-2].split()[1]

        

Rew = np.zeros((Num_States,Num_Actions,Num_States))
gamma = float(Lines[len(Lines)-1].split()[1])
for i in range(4,len(Lines)-2):
    Trans[int(Lines[i].split()[1])][int(Lines[i].split()[2])][int(Lines[i].split()[3])] = float(Lines[i].split()[5])
    Rew[int(Lines[i].split()[1])][int(Lines[i].split()[2])][int(Lines[i].split()[3])] = float(Lines[i].split()[4])
  
if(algorithm == "vi"):
    Policy, Val = vi(Num_States,Num_Actions,Trans,Rew, gamma) 
if(algorithm == "hpi"):
    Policy, Val =hpi(Num_States,Num_Actions,Trans,Rew, gamma) 
if(algorithm == "lp"):
    Policy, Val =lp(Num_States,Num_Actions,Trans,Rew, gamma)                 

for i in range(Num_States):
    print(np.round_(Val[i], decimals = 6),Policy[i])