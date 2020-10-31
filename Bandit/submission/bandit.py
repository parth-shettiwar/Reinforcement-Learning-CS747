import numpy as np



# print(a)
# print(c.shape)


def greedy(randomSeed,epsilon,horizon):
    
    coun = np.zeros((a.shape))
    pull_nums = np.zeros((a.shape))
    np.random.seed(randomSeed)
    for i in range(len(a)):
        rew = reward(i)
        coun[i] += rew
        pull_nums[i] += 1
    
    for i in range(horizon-len(a)):
        pull = np.random.choice([0, 1], size=(1,), p=[epsilon,1-epsilon])
        if(pull==0):
            arm_num = np.random.randint(len(a),size=1)
            rew = reward(arm_num[0])
            coun[arm_num[0]] += rew
            pull_nums[arm_num[0]] += 1
        if(pull==1):
            arm_high = np.argmax(np.divide(coun,pull_nums))
            rew = reward(arm_high) 
            coun[arm_high] += rew 
            pull_nums[arm_high] += 1 
    return(np.max(a)*horizon - np.sum(coun))       
def UCB(randomSeed,epsilon,horizon):
    np.random.seed(randomSeed)
    coun = np.zeros((a.shape))
    pull_nums = np.zeros((a.shape))
    ucb = np.zeros((a.shape))
    for i in range(len(a)):
        rew = reward(i)
        coun[i] += rew
        pull_nums[i] += 1
    for i in range(horizon-len(a)):
        ucb = np.divide(coun,pull_nums) + np.sqrt(np.divide(2*np.log(i+len(a)),pull_nums))
        arm_high = np.argmax(ucb)
        rew = reward(arm_high) 
        coun[arm_high] += rew 
        pull_nums[arm_high] += 1   
    return(np.max(a)*horizon - np.sum(coun))
def KLUCB(randomSeed,epsilon,horizon):
    np.random.seed(randomSeed)
    coun = np.zeros((a.shape))
    pull_nums = np.zeros((a.shape))    
    for i in range(len(a)):
        rew = reward(i)
        coun[i] += rew
        pull_nums[i] += 1
    for i in range(horizon-len(a)):
        ucb = klucb_opt(coun,pull_nums,i+len(a))
        arm_high = np.argmax(ucb)
        rew = reward(arm_high) 
        coun[arm_high] += rew 
        pull_nums[arm_high] += 1 
    return(np.max(a)*horizon - np.sum(coun))

def Thomson(randomSeed,epsilon,horizon):
    np.random.seed(randomSeed)
    coun = np.zeros((a.shape))
    pull_nums = np.zeros((a.shape))
    coun = np.zeros((a.shape))
    pull_nums = np.zeros((a.shape))     
    for i in range(horizon):
        arm = thomson(coun,pull_nums)
        rew = reward(arm) 
        coun[arm] += rew 
        pull_nums[arm] += 1   
    return(np.max(a)*horizon - np.sum(coun))
       

def Thomson_Hint(permuted_means,randomSeed,epsilon,horizon):
    np.random.seed(randomSeed)
    coun = np.zeros((a.shape))
    pull_nums = np.zeros((a.shape))
    belief = (1/len(a))*np.ones((len(a),len(a)))
     
    
    for i in range(horizon):
        arm = np.argmax(belief[:,np.argmax(permuted_means)])
        rew = reward(arm) 
        coun[arm] += rew 
        pull_nums[arm] += 1 
        belief[arm] = belief[arm]*(1*(1-rew) + pow(-1,(1-rew))*permuted_means)/np.sum(belief[arm]*(1*(1-rew) + pow(-1,(1-rew))*permuted_means))
    # print(pull_nums)
    return(np.max(a)*horizon - np.sum(coun))

    
def KL(x,y):
    if(y==0):
        return 0
    elif(x==0):
        return -np.log(1-y)
    else:

        return(x*np.log(x/y)+(1-x)*np.log((1-x)/(1-y)))
   
def klucb_opt(coun,pull_nums,iter):
    ucb_tem = np.zeros(len(coun))
    for i in range(len(coun)):
        up = 0.999
        em = coun[i]/pull_nums[i]
        low = coun[i]/pull_nums[i]
        const = np.log(iter) + 3*np.log(np.log(iter))
        while(up-low>0.001):
            mid = (up+low)/2
            if(pull_nums[i]*KL(em,mid)<=const):
                low = mid
            else:
                up = mid            
        ucb_tem[i] = low
        
    return(ucb_tem)    

 
def thomson(coun,pull_nums):
    maxx = 0
    arm_ind = 0
    temp = np.random.beta(coun+1,pull_nums-coun+1)
    return np.argmax(temp) 

def reward(ind):
    rew = np.random.choice([0, 1], size=(1,), p=[1-a[ind],a[ind]])
    return rew

# a = np.loadtxt("/home/adminpc/Documents/FILA/Prog/cs747-pa1/instances/i-1.txt")
# b = np.loadtxt("/home/adminpc/Documents/FILA/Prog/cs747-pa1/instances/i-2.txt")
# c = np.loadtxt("/home/adminpc/Documents/FILA/Prog/cs747-pa1/instances/i-3.txt")


import sys
instance = sys.argv[2]
algorithm  = sys.argv[4]
randomSeed =  int(sys.argv[6])
epsilon  = float(sys.argv[8])
horizon = int(sys.argv[10])
global a 
a = np.loadtxt(instance)

if(algorithm=="epsilon-greedy"):
    reg = greedy(randomSeed,epsilon,horizon) 
if(algorithm=="ucb"):
    reg = UCB(randomSeed,epsilon,horizon)
if(algorithm=="kl-ucb"):
    reg = KLUCB(randomSeed,epsilon,horizon)
if(algorithm=="thompson-sampling"):
    reg = Thomson(randomSeed,epsilon,horizon)
if(algorithm=="thompson-sampling-with-hint"): 
    permuted_means= np.sort(a) 
    reg = Thomson_Hint(permuted_means,randomSeed,epsilon,horizon)  
lis = [] 
# lis.append(instance,,,,horizon,reg)  
lis.append(sys.argv[2])
lis.append(sys.argv[4]) 
lis.append(sys.argv[6])
lis.append(sys.argv[8])
lis.append(sys.argv[10])
lis.append(str(reg))
print(', '.join(lis))
