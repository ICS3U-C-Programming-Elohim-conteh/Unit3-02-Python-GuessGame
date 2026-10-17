#!/usr/bin/env python3
# Created by:elohim
# Created on: Oct 13 2026
# This program asks the user to guess a number and checks if it is correct or not.

CORRECT_ANSWER = 7


def main():
    # Get number from user between 0 and 9 and convert to an integer
    number = int(input("Enter a number between 0 and 9: "))

    # Check if number == correct answer
    if number == CORRECT_ANSWER:

        # Display you are correct and show the correct answer
        print("You are correct")

    # Check if number != correct answer
    if number != CORRECT_ANSWER:

        # Display you are not correct to the user and show the correct answer
        print("You are not correct. The correct answer is {}".format(CORRECT_ANSWER))


if __name__ == "__main__":
    main()
