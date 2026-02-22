import random #imports the random module
myno = random.randint(1, 100)
attempts = 0
guess = None #both attempt and guess are our varibalkes so we can call them later
low, high =1,100 #initial range
# welcome msg
print("hello, welcome to Nidhi's guess game")
print(" can u guess what number am i thinking between 1 to 100")
while guess!= myno: # while loops mean keep running the code inside this block as long as the condition is true 
    guess = int(input("enter your guess:"))
    attempts += 1 # attempts = attempts + 1
# in this case keep running the loop until the users guess is equal to the number
# Once the guess is correct, the condition becomes false, and the loop stops.
#int(input converts the user input into integer otherwise it will be saved as a string
   
    if guess < myno:
        print("too low, try again")
        low = guess +1 # update lower bound
        print(f"HINT: try between {low} and {high}")
    elif guess > myno:
        print("too high, try again!")
        high = guess - 1  # update upper bound
        print(f"HINT: try between {low} and {high}")
    else:
        print("yay you have guessed right")
        print(f"you guessed it in {attempts} attempys")
        #Anything inside {} gets replaced with the value of that variable when the string is printed.
