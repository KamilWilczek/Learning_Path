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


# import itertools


# def permutations(string):
#     return set("".join(x) for x in itertools.permutations(string, r=len(string)))
