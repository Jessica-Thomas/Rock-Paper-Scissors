import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

# intakes user's choice
def get_user_selection():
    user_input = input("Choose your weapon: Rock[0], Paper[1], Scissors[2]):  ")
    selection = int(user_input)
    action = Action(selection)
    return action


# randomly selects computer's choice
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


