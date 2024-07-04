import random

def get_player_choice():
    choices = input("Enter Your Choice: - (stone , paper , sessisor)").lower()
    while choices not in ["stone" , "paper" , "sessisor"]:
        choices = input("Invaild Choce! Enter Your Choice: - [stone , paper , sessisor]").lower()
    return choices

def random_choice():
    choices = ["stone" , "paper" , "sessisor"]
    return random.choice(choices)

def winner(player , random):
    if player == random:
        return "Draw!"
    elif player == "Stone" and random == "Sessisor":
        return "You Win"
    elif player == "Sessisor" and random == "Paper":
        return "You Win"
    elif player == "Paper" and random == "Stone":
        return "You Win"
    else:
        return "Robot Wins"

def game():
    while True:
        player = get_player_choice()
        random = random_choice()
        print(f"Robot Choosed:-  {random_choice}")

        result = winner(player , random)
        print(result)
        play_again = input("Want to play Again yes/no").lower()
        if play_again != "yes":
            break

    print("Exiting....")

if __name__ =="__main__":
    game()
