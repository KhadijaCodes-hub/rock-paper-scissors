import random

user_wins=0
comp_wins=0
options=["rock","paper","scissor"]

while True:
    user_input = input("(Type Rock/Paper/Scissor) or (Type Q to quit). ").lower()

    if user_input=="q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0 : rock , 1: paper , 2: scissor
    comp_pick=options[random_number]
    print(f"Computer picked {comp_pick}.")

    if user_input=="rock" and comp_pick=="scissor":
        print("You Won!")
        user_wins+=1
    elif user_input=="paper" and comp_pick=="rock":
        print("You Won!")    
        user_wins+=1
    elif user_input=="scissor" and comp_pick=="paper":
        print("You Won!")
        user_wins+=1
    else:
        print("You Lost!")
        comp_wins+=1    

print(f"You Won {user_wins} times.")
print(f"Computer Won {comp_wins} times.")
print("Goodbye!")