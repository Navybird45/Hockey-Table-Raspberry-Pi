import os
import random
import time


#  vvv Below Here Can Be Edited vvv
team_1_name = "team1"
team_2_name = "team2"
team_1_score_clips = [
    "team one score clip 1", "team one score clip 2", "team one score clip 3"
]
team_2_score_clips = [
    "team two score clip1", "team two score clip2", "team two score clip3"
]
team_1_win_clips = [
    "team one win clip 1", "team one win clip 2", "team one win clip 3"
]
team_2_win_clips = [
    "team two win clip1", "team two win clip2", "team two win clip3"
]
#  ^^^^ Above Here Can Be Edited ^^^^
team_1_score = 0
team_2_score = 0


def welcome():
    print("Welcome to the Game!")
    help_screen()


def help_screen():
    """Displays the help screen"""
    print("""
    Enter team names and link to clips at the top of the script;
    Enter the number of the team who scores;
    Enter 'Quit' to quit;
    Enter 'Help' to get to this menu.
    """)


def tell_score():
    print("The current score is:\n {}: {}\n {}: {}".format(
          team_1_name, team_1_score, team_2_name, team_2_score))


def clear_screen():
    """Looks at system;
    Runs 'nt' for all modern versions of Windows;
    Runs 'clear' if on a non-Windows computer;
    """
    os.system("cls" if os.name == "nt" else "clear")


def game_loop():
    global team_1_score
    global team_2_score
    game_type = input("Is this a (1)scored, (2)freeplay, or (3)timed game?")
    if game_type == "1":
        win_score = int(input("What's the score limit? > "))
        while True:
            clear_screen()
            tell_score()
            who_scores = input("Who scores? (number)\n1. {} or 2. {} \n > "
                               .format(team_1_name, team_2_name))
            if who_scores == "1":
                team_1_score += 1
                if team_1_score < win_score:
                    input(random.choice(team_1_score_clips))
                    continue
                elif team_1_score >= win_score:
                    input(random.choice(team_1_win_clips))
                    input("{} wins!".format(team_1_name))
                    break
            elif who_scores == "2":
                team_2_score += 1
                if team_2_score < win_score:
                    input(random.choice(team_2_score_clips))
                    continue
                elif team_2_score >= win_score:
                    input(random.choice(team_2_win_clips))
                    input("{} wins!".format(team_2_name))
                    break
            else:
                input("Incorrect Command")
                continue
            break
    elif game_type == "2":
        while True:
            tell_score()
            who_scores = input("Who scores? (number)\n1. {} or 2. {} \n > "
                               .format(team_1_name, team_2_name))
            if who_scores == "1":
                team_1_score += 1
                input(random.choice(team_1_score_clips))
                continue
            elif who_scores == "2":
                team_2_score += 1
                input(random.choice(team_2_score_clips))
            elif who_scores == "Quit":
                break
            else:
                input("Incorrect Command")
                continue
    elif game_type == "3":
        number_of_minutes = int(input("How many minutes?"))
        timeout = time.time() + 60 * number_of_minutes   # 5 minutes from now
        while True:
            test = 0
            if test == 5 or time.time() > timeout:
                if team_1_score > team_2_score:
                    input(random.choice(team_1_win_clips))
                    tell_score()
                elif team_2_score > team_1_score:
                    input(random.choice(team_2_win_clips))
                    tell_score()
                elif team_1_score == team_2_score:
                    input(random.choice(team_1_win_clips))
                    input(random.choice(team_1_win_clips))
                break
            test = test - 1
            clear_screen()
            tell_score()
            who_scores = input("Who scores? (number)\n1. {} or 2. {} \n > "
                               .format(team_1_name, team_2_name))
            if who_scores == "1":
                team_1_score += 1
                input(random.choice(team_1_score_clips))
                continue
            elif who_scores == "2":
                team_2_score += 1
                input(random.choice(team_2_score_clips))
            elif who_scores == "Quit":
                break
            else:
                input("Incorrect Command")
                continue
    else:
        input("Incorrect Command")


if __name__ == '__main__':
    welcome()
    game_loop()
