# Rock Paper Scissors Project

def User2(UserOneAsk: str):  
    UserTwoAsk = 0
    UserTwoAsk = (input("User 2 enter Rock, Paper, or Scissors ,please include uppercase letters for beginning of word."))
    print(UserTwoAsk)
    if UserTwoAsk == "Rock" or "Paper" or "Scissors":
        print("ok, now for the results")
        winner(UserOneAsk,UserTwoAsk)
    elif UserTwoAsk != "Rock" or "Paper" or "Scissors":
        print("Please restart and enter Rock, Paper, or Scissors ONLY.")

# This is where the main code is
def main():
    # Variables
    UserOneAsk = 0 # UserOneAsks User 1
    UserOneAsk = str(input("User 1 enter Rock, Paper, or Scissors ,please include uppercase letters for beginning of word."))
    print(UserOneAsk)
    if UserOneAsk == "Rock" or UserOneAsk == "Paper" or UserOneAsk == "Scissors" :
        print("ok, now for you User 2")
        User2(UserOneAsk = UserOneAsk)
    elif UserOneAsk != "Rock" or UserOneAsk != "Paper" or UserOneAsk != "Scissors":
        print("Please restart and enter Rock, Paper, or Scissors ONLY.")
    return()

# This function determines the winner
def winner(UserOneAsk, UserTwoAsk):
    if UserOneAsk == "Rock" and UserTwoAsk == "Rock":
        print("Draw")
    elif UserOneAsk == "Paper" and UserTwoAsk == "Paper":
        print("Draw")
    elif UserOneAsk == "Scissors" and UserTwoAsk == "Scissors":
        print("Draw")
    elif UserOneAsk == "Rock" and UserTwoAsk == "Scissors":
        print("User 1 wins")
    elif UserOneAsk == "Paper" and UserTwoAsk == "Rock":
        print("User 1 wins") 
    elif UserOneAsk == "Scissors" and UserTwoAsk == "Rock":
        print("User 2 wins")
    elif UserOneAsk == "Rock" and UserTwoAsk == "Paper":
        print("User 2 wins")
    elif UserOneAsk == "Paper" and UserTwoAsk == "Scissors":
        print("User 2 wins")
    
       

# This is where the main function is called
if __name__ == '__main__':
    main()