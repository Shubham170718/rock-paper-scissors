import random

# Game Function
def game_result(computer_choice,your_choice):
    
    # Tie condition
    if computer_choice==your_choice:
        return None
    
    # All possibilities when computer choice is Rock
    if computer_choice=="r":
        if your_choice=="p":
            return True
        elif your_choice=="s":
            return False

    # All possibilities when computer choice is paper   
    if computer_choice=="p":
        if your_choice=="s":
            return True
        elif your_choice=="r":
            return False

    # All possibilities when computer choice is Scissor
    if computer_choice=="s":
        if your_choice=="r":
            return True
        elif your_choice=="p":
            return False        

# Computer choice
print("Computer_turn:Rock(r),Paper(p),Scissor(s)")
computer_choice=random.randint(1,3)
if computer_choice==1:
    computer_choice="r"
elif computer_choice==2:
    computer_choice="p"
elif computer_choice==3:
    computer_choice="s" 

# Player choice
your_choice=input("your_choice:Rock(r),Paper(p),Scissor(s)?:")

# Computer and player choice
print(f"Computer choice is {computer_choice}")
print(f"Your choice is {your_choice}")

# Calling of game function
Result=game_result(computer_choice,your_choice)

# Game result prediction
if Result==None:
    print("The game is tie")
elif Result:
    print("You win!")
else:
    print("You lose!")        


    