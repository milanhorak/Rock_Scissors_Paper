#!/usr/bin/env python3

import random
from enum import Enum


class Choice(Enum):
    Rock = "r"
    Paper = "p"
    Scissors = "s"
    Quit = "q"


def get_user_sel(choices_str: str) -> Choice:
    selection = input(f"\nEnter a choice ({choices_str}): ").lower()
    choice = Choice(selection)
    return choice


def get_computer_sel(choices_val: list[str]) -> Choice:
    # eliminate Choice.Quit
    selection = random.choice(choices_val[:3])
    choice = Choice(selection)
    return choice


def determine_winner(user_choice: Choice, computer_choice: Choice) -> bool | None:
    # combination of victories
    victories = {
        Choice.Rock: Choice.Scissors,     # Rock beats scissors
        Choice.Paper: Choice.Rock,        # Paper beats rock
        Choice.Scissors: Choice.Paper     # Scissor beats paper
    }
    # selection from dictionary , who you defeat
    defeats = victories[user_choice]
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice.name}. It's a tie!")
        return None
    elif computer_choice == defeats:
        print(f"{user_choice.name} beats {computer_choice.name}! You win!")
        return True
    else:
        print(f"{computer_choice.name} beats {user_choice.name}! You lose.")
        return False


def main():
    # set variables
    sepa = "*" * 55
    choices: list[str] = [f"[{choice.value}]{choice.name[1:]}" for choice in Choice]
    choices_str: str = ", ".join(choices)
    choices_val: list[str] = [choice.value for choice in Choice]
    user_wins, computer_wins, ties = 0, 0, 0

    # greeter
    print(
        sepa, "Welcome to Rock Scissors Paper game.", "You can quit the game any time, just enter [q].", sepa, sep="\n"
    )

    while True:
        # user choice
        try:
            user_choice: Choice = get_user_sel(choices_str)
            # want to quit ?
            if user_choice == Choice.Quit:
                break
        except ValueError:
            print(f"Invalid selection. Enter any from {choices_val}")
            continue
        print(f"You: {user_choice.name}")

        # computer choice
        computer_choice: Choice = get_computer_sel(choices_val)
        print(f"Computer: {computer_choice.name}")

        # get winner
        winner: bool | None = determine_winner(user_choice, computer_choice)

        # update score
        if winner is None:
            ties += 1
        elif winner:
            user_wins += 1
        else:
            computer_wins += 1

    # print score
    print(sepa, f"You: {user_wins} wins", f"Computer: {computer_wins} wins", f"Ties: {ties}", sepa, sep="\n")


if __name__ == '__main__':
    main()
