****Assignment 3 CS747****  

Contains 2 codes: Windy.py and data_gen.py. plots folder contains all plots put in the report.  
Windy.py contains all code for for 3 algorithms and overall MDP.  
data_gen.py contains the code to generate plots.  
run **python data_gen.py** to generate all the plots given in the report (all for 171 episodes) in the current directory. For generating a   high time step plot, just change the number of episodes in the while loop in Windy.py. The main MDP function from Windy.py is called in   data_gen.py always. It takes the following paramters:  
1)Algorithms : 0 for Q-learning,1 for Sarsa and 2 for Expected sarsa  
2)Number of moves: 4 or 8  
3)Alpha(decide the learning rate): anything between 0 to 1  
4)Epsilon(decide the amount of exploration): anything between 0 to 1   
5)stoch: can be 0 or 1. 0 for no stochasticity and 1 for stochasticity.  
6)seed value: can be any integer  
All simulations dont take more than 5 minutes to run.  
