# --- Part Two ---

# To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

# To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

# J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

# Now, the above example goes very differently:

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

#     32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
#     KK677 is now the only two pair, making it the second-weakest hand.
#     T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

# With the new joker rule, the total winnings in this example are 5905.

# Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?

import os
import re
from functools import cmp_to_key
from collections import Counter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay7.txt"))
puzzle_input = f.read()


def part1(puzzle_input):

    def get_type(hand):
        counts = sorted(Counter(hand).values(), reverse=True)
        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts[0] == 3 and counts[1] == 2:
            return 4
        if counts[0] == 3:
            return 3
        if counts[0] == 2 and counts[1] == 2:
            return 2
        if counts[0] == 2:
            return 1
        return 0

    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = cards.index(card_a) > cards.index(card_b)
            return 1 if a_wins else -1

    cards = "23456789TJQKA"
    regex = r"(\w{5}) (\d+)"
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)
    return total


def part2(puzzle_input):

    def get_type(hand):
        jokers = hand.count("J")
        hand = [c for c in hand if c != "J"]
        counts = sorted(Counter(hand).values(), reverse=True)
        if not counts:
            counts = [0]
        if counts[0] + jokers == 5:
            return 6
        if counts[0] + jokers == 4:
            return 5
        if counts[0] + jokers == 3 and counts[1] == 2:
            return 4
        if counts[0] + jokers == 3:
            return 3
        if counts[0] == 2 and (jokers or counts[1] == 2):
            return 2
        if counts[0] == 2 or jokers:
            return 1
        return 0

    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = cards.index(card_a) > cards.index(card_b)
            return 1 if a_wins else -1

    cards = "J23456789TQKA"
    regex = r"(\w{5}) (\d+)"
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)
    return total


print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))
