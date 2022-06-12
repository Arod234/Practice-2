import random


#functions
def intro():
    print("Hello traveler")
    print("It has looked like you just came in my cave uninvited")
    print("Now for your punishment you must go through my very specific cave tunnel system to get out alive")
    print("If you dont accept I will call the ploice for breaking and entering, I don't want to call the police so I will limit your response to this to: Yes I want to go to the caves")
    

    
  
def cave_choice():
    
    
    cave =input("Ah great you don't want to spend 5-12 years in prison, so traveler which cave will it be green or black")
    
    cave=cave.upper()
    
    return cave

def cave_black():
    
    print("You find a burrito in the middle of the floor, do you pick it up and eat it?") 
        
    choice2 = input("Do you want to eat it?")
    choice2= choice2.upper()
    
    if(choice2 == "YES"):
        print("You get sick and die because it had bad meat in it")
        
        
    elif(choice2 == "NO"):
        print("You see 2 more tunnels and the two say deadly cave and good cave.")
        black_choice()
        
def black_choice():
    print("You are uncertain of which cave to go but you don't care and just want to go home")
    choice7=input("Which cave do you go in? Deadly where you will die or good where you also can die")
    choice7=choice7.upper()
    if(choice7 == "DEADLY"):
        print("Despite it being called Deadly cave it doesn't kill you, but you see a door called dragon,you don't know if you want to stay or go in")
        deadly_cave()
        
        
    elif(choice7== "GOOD"):
        print("The cave you thought was good wasn't good at all it was trash a actually demon bat bossbattle is going on, you can ignore it or push it")
        good_cave()
def cave_green():
    print("You are in a room in a room and there are two mysterious doors next to you, one saying death the other one saying life")
    choice3 = input("Which door do you want to enter?")
    choice3 = choice3.upper()
    
    if(choice3== "LIFE"):
        print("You see Jesus and he says don't go through the bad hole on the right and dissapears, now you see two holes one is on the left the other is on the right")
        cave_life()
    elif(choice3 == "DEATH"):
        print("You see the Devil himself and he leads you to two old shabby doors one saying Restroom and one saying escape")
        cave_death()

def cave_life():
    print("After telling jesus that you would go down the left hole you slide down the hole and you get hurt, once you wake up you see something its a big dragon or the way out")
    choice4= input("What do you see?")
    choice4= choice4.upper()
    
    if(choice4== "DRAGON"):
        print("Well you die because its a dragon and you don't have tools to kill it like you cant punch a dragon and kill it in one shot")
    elif(choice4=="Escape"):
        print("You escape and get to see your family woohoo")
        
def cave_death():
    print("You ask the evil man if he could trust him and he says no but one of them are safe")
    choice5=input("Will you choose the restroom or Escape")
    choice5= choice5.upper()
    if(choice5== "RESTROOM"):
        print("You use the restroom and the toilet sucks you in and pops you out a sewer pipe and you escaped")
    elif(choice5 =="ESCAPE"): 
        
        print("You see a wizard and he says wow you fell for the oldest trick in the book and then he kills you with his powers")
        
def deadly_cave():
    print("You still do not know what to do, go to Dragon or Wait")
    choice8=input("Dragon or Wait")
    choice8=choice8.upper()
    
    if(choice8== "DRAGON"):
        print("You see a dragon, steal his milk and walk past it and make it to the exit, you win the game")
        
    elif(choice8 == "WAIT"):
        print("Someone out of no where kills you with Scream 4, never underestimate bad sequels")
        
def good_cave():
    print("You know have two choices")
    choice9=input("Ignore or Push")
    choice9=choice9.upper()
    
    
    if(choice9== "IGNORE"):
        print("You ignore it and the demon bat kills you cause it has a brain")
        
    elif(choice9== "PUSH"):
        print("With Hercules strength you push of the bat with max health and slay it then make it out of the cave and to your lovling family")
        

#Main    
playAgain = "yes"
while playAgain == "yes":
    intro()
    
    choice = cave_choice()
    if choice == "BLACK":
        cave_black()
    if choice == "GREEN":
        cave_green()
    
  
                           
    playAgain = input("Do you want to play again?")
    