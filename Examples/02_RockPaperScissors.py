import random

count = 1
player_score = 0
while (count < 4):        

    computer = int(random.randint(0, 2))
    if computer == 0:
        c_choice = "rock"
    elif computer == 1:
        c_choice = "paper"
    else:
        c_choice = "scissors"

    p_choice = str(input("Round 1: Enter rock, paper, or scissors [R/ P/ S]"))

    print(f"computer: {c_choice}")
    if p_choice == "R":
        if c_choice == "rock":
            print("draw! - play again")
        elif c_choice == "paper":
            print(f"computer wins round {count}!")
            count += 1
        else:
            print(f"you win round {count}!")
            count += 1
            player_score += 1

    elif p_choice == "P":
        if c_choice == "rock":
            print(f"you win round {count}!")
            count += 1
            player_score += 1
        elif c_choice == "paper":
            print("draw! - play again")
        else:
            print(f"computer wins round {count}!")
            count += 1

    else:
        if c_choice == "rock":
            print(f"computer wins round {count}!")
            count += 1
        elif c_choice == "paper":
            print(f"you win round {count}!")
            count += 1
            player_score += 1
        else:
            print("draw! - play again")

if player_score >= 2:
    print("you win!")

else: 
    print("you lose!")


