import numpy as np
import sys 
import matplotlib.pyplot as plt
import Windy
from Windy import MDP
dic = {0:"Q Learning", 1:"Sarsa", 2:"Expected Sarsa"}
print("Generating results for Combine 4 move case")
plt.figure()
for i in range(3):
  
  run_x = np.zeros((172))
  for j in range(10):
    y,x = MDP(i ,4, aplha = 0.5, epsilon = 0.1,stoch = 0,seed = j) 
    run_x = x + run_x
  plt.plot(run_x/10,y,label = dic[i])
  plt.grid(True)
plt.xlabel('Time Steps')
plt.ylabel('Episodes')  
plt.legend(loc='best')
plt.savefig('combine.png')
print("Generating results for Combine king moves case")
plt.figure()
for i in range(3):
  run_x = np.zeros((172))
  for j in range(10):
    y,x = MDP(i ,8, aplha = 0.5, epsilon = 0.1,stoch = 0,seed = j) 
    run_x = x + run_x
  plt.plot(run_x/10,y,label = dic[i])
  plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Time Steps')
plt.ylabel('Episodes') 
plt.savefig('combine-king.png')
print("Generating results for Sarsa normal case")
plt.figure()
run_x = np.zeros((172))
for j in range(10):
  y,x = MDP(1 ,4, aplha = 0.5, epsilon = 0.1,stoch = 0,seed = j) 
  run_x = x + run_x
plt.plot(run_x/10,y,label = "Sarsa-Normal")
plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Time Steps')
plt.ylabel('Episodes') 
plt.savefig('sarsa.png') 

print("Generating results for Sarsa king moves case")
plt.figure()
run_x = np.zeros((172))
for j in range(10):
  y,x = MDP(1 ,8, aplha = 0.5, epsilon = 0.1,stoch = 0,seed = j) 
  run_x = x + run_x
plt.plot(run_x/10,y,label = "Sarsa-King")
plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Time Steps')
plt.ylabel('Episodes') 
plt.savefig('sarsa-king.png')

print("Generating results for Sarsa king moves with Stochasticity case")
plt.figure()
run_x = np.zeros((172))
for j in range(10):
  y,x = MDP(1 ,8, aplha = 0.5, epsilon = 0.1,stoch = 1,seed = j) 
  run_x = x + run_x
plt.plot(run_x/10,y,label = "Sarsa-king with Stochasticity")
plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Time Steps')
plt.ylabel('Episodes') 
plt.savefig('sarsa-stock-king.png')

print("Generating results for Sarsa with epsilon variation")
plt.figure()
for i in range(4):
  run_x = np.zeros((172))
  for j in range(10):
    y,x = MDP(1 ,4, aplha = 0.5, epsilon = 0.05*(i+1),stoch = 0,seed = j) 
    run_x = x + run_x
  plt.plot(run_x/10,y,label = "Epsilon=%s" %(str(round(0.05*(i+1),2))) )
  plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Time Steps')
plt.ylabel('Episodes') 
plt.savefig('sarsa-epsilon.png')

print("Generating results for Sarsa with alpha variation")

plt.figure()
for i in range(4):
  run_x = np.zeros((172))
  for j in range(10):
    y,x = MDP(1 ,4, aplha = (0.2+0.15*i), epsilon = 0.1,stoch = 0,seed = j) 
    run_x = x + run_x
  plt.plot(run_x/10,y,label = "Alpha=%s" %(str(round((0.2+0.15*i),2))))
  plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Time Steps')
plt.ylabel('Episodes') 
plt.savefig('sarsa-aplha.png')  

print("Generating results for Combine 4 move with Stochasticity")

plt.figure()
for i in range(3):
  
  run_x = np.zeros((172))
  for j in range(10):
    y,x = MDP(i ,4, aplha = 0.5, epsilon = 0.1,stoch = 1,seed = j) 
    run_x = x + run_x
  plt.plot(run_x/10,y,label = dic[i])
  plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Time Steps')
plt.ylabel('Episodes') 
plt.savefig('combine-with-stoch.png')

