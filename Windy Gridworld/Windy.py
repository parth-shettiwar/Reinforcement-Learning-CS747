import numpy as np
import sys 

H = 7
B = 10
num_states = 70
winds = np.zeros((10))
winds[3] = 1
winds[4] = 1
winds[5] = 1
winds[6] = 2
winds[7] = 2
winds[8] = 1 
def MDP(algorithm = 0,num_actions=8, aplha = 0.5, epsilon = 0.1,stoch = 0,seed = 0):
  np.random.seed(seed)
  Policy = np.zeros((num_states))
  start = 30
  end = 37
  reward_grid = -1*np.ones((num_states)) 
  reward_grid[37] = 1
  tot = np.zeros((1))
  zz = np.zeros((1))
  Q = np.zeros((num_states,num_actions))
  eps = 0
  coun = 0
  run_sum = 0
  while(eps<=170):
    new_state = start
    curr = start
    coun = 0
    act_ls = []
    while(new_state!=end):

      curr = new_state
      act = int(action_take(curr,Policy,epsilon,num_actions))
      new_state = int(new_st(curr, act,stoch))
      act2 = int(action_take(new_state,Policy,epsilon,num_actions))
      rew = reward_grid[new_state]
      if(algorithm == 0):
        Target = rew + np.max(Q[new_state])
      if(algorithm == 1):
        Target = rew + Q[new_state,act2] 
      if(algorithm == 2):
        temp = np.zeros((num_actions))
        temp[int(Policy[new_state])] = 1
        pi = (epsilon/num_actions) * np.ones((num_actions)) + (1-epsilon)*temp
        Target = rew + np.sum(rew + pi*Q[new_state]) 

      Q[curr,act] = Q[curr,act] + aplha*(Target-Q[curr,act])
      Policy = np.argmax(Q,axis=1)
      coun = coun + 1
      act_ls.append(act)
    
    eps = eps + 1
      
    run_sum = run_sum + coun 
    zz = np.append(zz,eps)
   
    tot = np.append(tot,run_sum)
  
  return  zz,tot
     




    
def action_take(state,Policy,epsilon,num_actions):
  a = np.random.choice(2, 1, p=[epsilon,1-epsilon])
  if(int(a) == 0):
    act = np.random.randint(num_actions, size=1)
  if(int(a) == 1):
    act = Policy[state] 
  return act  
#0 = up, 1 = down. 2 = right, 3 = left  ,  4 = tl, 5 = tr, 6 = dl, 7 = dr   
#0 = go up extra 1 = normal 2 = go down extra
def new_st(state,action,stoch):
  x = state%10
  y = int(state/10)
  num = 0
  if(stoch):
    num = np.random.randint(3, size=1)
    num = num - 1
  if(action == 0):
    y = min(max(y - winds[x] - 1 + num,0),6)
  elif(action == 1):
    y = min(max(y - winds[x] + 1 + num,0),6)    
  elif(action == 2):
     
    y = min(max(y - winds[x] + num,0),6)
    x = min(x+1,9)
  elif(action == 3):
    
    y = min(max(y - winds[x] + num,0),6)
    x = max(x-1,0)


  elif(action == 4):
    y = min(max(y - winds[x] - 1 + num,0),6)
    x = max(x-1,0) 
  elif(action == 5):
    y = min(max(y - winds[x] - 1 + num,0),6)  
    x = min(x+1,9)  
  elif(action == 6):
    y = min(max(y - winds[x] + 1 + num,0),6)
    x = max(x-1,0)
  elif(action == 7):
    
    y = min(max(y - winds[x] + 1 + num,0),6)
    x = min(x+1,9)  
  new_state = y*B + x 
  return new_state    


