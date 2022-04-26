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


input_string = "aabb"


def permutations(input_string):
    pool = tuple(input_string)
    n = len(pool)
    index_list = list(range(n))
    cycles = list(range(n, 0, -1))
    yield str(pool[i] for i in index_list[:n])
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                index_list[i:] = index_list[i + 1 :] + index_list[i : i + 1]
                cycles[i] = n - 1
            else:
                j = cycles[i]
                index_list[i], index_list[-j] = index_list[-j], index_list[i]
                yield tuple(pool[i] for i in index_list[:n])
                break
        else:
            return


# string_list = []
# index_list = []

# for letter in input_string:
#     string_list.append(letter)
# print(string_list)

# # for i, item in enumerate(string_list):
# #     index_list.append(i)
# # print(index_list)

# for i, item in enumerate(string_list):
#     try:
#         print(string_list[i] + string_list[i + 1])
#     except:
#         print(string_list[i] + string_list[0])
