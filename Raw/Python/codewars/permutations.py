"""
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:
* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""


def permutations(string):
    if len(string) == 0:
        return []

    elif len(string) == 1:
        return [string]

    else:
        return set(
            string[index] + p
            for index in range(len(string))
            for p in permutations(string[:index] + string[index + 1 :])
        )


# Best Practice
import itertools


def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


def permutations(string):

    # using tools to create permuatations of the input string
    from itertools import permutations

    perm = permutations(string)
    # putting permutations into a dictionary to remove duplicates
    # and then putting the permutations back into a list
    perm_list = list(dict.fromkeys(perm))
    # joining the tuples in the permuation list together with empty apostrophes
    answer = ["".join(tups) for tups in perm_list]

    return answer
