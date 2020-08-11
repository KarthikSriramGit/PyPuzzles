"""
The Monty Hall problem is similar to the "ants on an equilateral triangle" problem in its approach to reaching a solution. 
For efficiency in problem-solving, the probability of all dependent variables need to be analyzed and a truth table needs to be utilized for deduction. 

Step by step solution process:

>Macro level, intuitive solution:
Focus on the initial probability of choosing a car or a goat. The probability of choosing a "goat" forms a direct relationship with the probability of winning by swapping. 
It can be seen that the choice to swap between doors will always be the favourable outcome as long as the number of goats is greater than the number of cars. 

>Micro level, breakdown solution:   

Below, the assumption is that door 1 is always chosen.
In the scenario of 3 doors and 1 car, the possible arrangements are:
1 2 3  Swap Keep
------------------
G G C  Win  Lose      # door 2 revealed.
G C G  Win  Lose      # door 3 revealed.
C G G  Lose Win       # either door 2 or 3 revealed.

In binary, if we were to assign 1 to G and 0 to C, 1 to Win and 0 to lose, and doors 1,2,3 as A,B,C:
A B C  Swap Keep
1 1 0  1    0              
1 0 1  1    0      
0 1 1  0    1      
With the above table, we can see that 
  1. To win by swapping forms 2/3rd of the total outcomes. 
  2. The possibility of winning by swapping corresponds to the presence of a "goat" in column A. Swap=A. 
Result: Better chance (66.67% or 2/3 for 3 doors) of winning when you chose to swap!
"""
import random #Library to generate a random number

def MontyHall(): 
    
    #print("Enter the number of doors") 
    doors = 3  #Extension possible here, while 'doors' not equal to 0.
    cars = 1   #Extension can be also made to the number of cars, while 'cars' less than 'doors' for the desired outcome.  
    
    print("Enter the number of simulations:")
    n = int(input())  #Example n = 10000 simulations, while 'n' not equal to 0.  
    win=0  # Initialization of win
    
    print("Enter choice '0' to always swap and '1' to always keep!")  #All other values are invalid which can be declared if necessary
    choice_keep=int(input()) #Choice entered to either always keep or always swap 
    
    for i in range(n):
        car_chosen =  random.random() <=cars/doors #Car getting chosen in our door(default car_chosen = 0/1) has maximum probability of no.of cars/no.of doors, 1/3 if 1 car and 3 doors.
        if(car_chosen==choice_keep): #Car_chosen = 1 and choice_keep = 1 or if both are 0, it results in a win (with Swap=A from the above table). 
          win += 1
    
    print("In ",n, "simulations, you would have won: ",win," and you would have lost:",n-win) # lost = no.of simulations - wins
    print("Probability of winning with your choice:", win/n * 100,"%") 

MontyHall()
