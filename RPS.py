

def main():
    one = input("User 1 Enter Rock, Paper, or Scissors: ")
    if one != "Rock" and one != "Paper" and one != "Scissors":
        print("Error: Enter Rock, Paper, or Scissors Only")
    two = input("User 2 Enter Rock, Paper, or Scissors: ")
    if two != "Rock" and two != "Paper" and two != "Scissors":
        print("Error: Enter Rock, Paper, or Scissors Only")
    print(RPS(one, two))

def RPS(one, two):
    if one == "Rock" and two == "Scissors":
        return "User 1 Wins!"
    elif one == "Rock" and two == "Paper":
        return "User 2 Wins!"
    elif one == "Paper" and two == "Rock":
        return "User 1 Wins!"
    elif one == "Paper" and two == "Scissors":  
        return "User 2 Wins!"
    elif one == "Scissors" and two == "Paper":
        return "User 1 Wins!"
    elif one == "Scissors" and two == "Rock":
        return "User 2 Wins!"
    else:
        return "Draw!"
    


if __name__=="__main__":
    main()