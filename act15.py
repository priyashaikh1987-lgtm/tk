import random
c = input("enter if you want to play rock paper scissors: ").lower()
while c == "yes":
    pc = input("enter rock paper or scissors: ").lower()
    cc = random.choice(["rock", "paper", "scissors"])
    if pc == cc:
        print("its a tie, the computer picked", cc)
    elif pc == "scissors" and cc == "paper":
        print("you win, the computer picked", cc)
    elif pc == "paper" and cc == "rock":
        print("you win, the computer picked", cc)
    elif pc == "rock" and cc == "scissors":
        print("you win, the computer picked", cc)
    elif pc == "rock" and cc == "paper":
        print("you lost, the computer picked ", cc)
    elif pc == "scissors" and cc == "rock":
        print("you lost, the computer picked ", cc)
    elif pc == "paper" and cc == "scissors":
        print("you lost, the computer picked ", cc)
    else:
        print("pick rock, paper, or scissors")