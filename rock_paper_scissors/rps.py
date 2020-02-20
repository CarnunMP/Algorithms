#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    # First thoughts: 
    #  - Number of possible plays is 3^n, where n is the number of plays per round.
    #  - Can think of possible plays as branches of a (decision) tree: a tree with 3^n branches.
    #  - First 'fork' (first decision) is ['rock', 'paper', 'scissors'].
    #  - Second 'fork' happens three times, once on each new branch, again between ['rock', 'paper', 'scissors'].
    #  - And so on.
    #  - In the end, a branch can be described by the sequence of 'decisions' made along the way to its tip.
    #  - This sequence will be n items long, with each taken from ['rock', 'paper', 'scissors'].

    if n == 0:
        return [[]]

    possible_plays = ['rock', 'paper', 'scissors']

    output = []
    possible_play_index = 0

    for i in range(3**n):
        output.append([possible_plays[possible_play_index]])

        if i % pow(3, n-1) == pow(3, n-1) - 1:
            possible_play_index = possible_play_index + 1 if possible_play_index < 2 else 0

    possible_play_index = 0
    additional_runs = n - 1
    for i in range(0, additional_runs):
        for j in range(3**n):
            output[j].append(possible_plays[possible_play_index])

            if j % pow(3, additional_runs - 1 - i) == pow(3, additional_runs - 1 - i) - 1:
                possible_play_index = possible_play_index + 1 if possible_play_index < 2 else 0

    return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')