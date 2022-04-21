# raise Exception('This is the error message.')
# """
#
# ***************
# *             *
# *             *
# *             *
# ***************
#
# """

# def box_print(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('"symbol" needs to be a string of length 1.')
#     if (width < 2) or (height < 2):
#         raise Exception('"width" and "height" must be greater or equal to 2.')
#
#     print(symbol * width)
#
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2) + symbol))
#
#     print(symbol * width)
#
#
# # box_print('**', 15, 5)
# # box_print('O', 5, 16)
# # box_print('*', 1, 1)


# # writes log of errors
# import traceback
# import os
#
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('error_log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written error_log.txt')
#
# print(os.getcwd())


# assert False, 'This is the error message.'

market_2nd = {'ns': 'green',
              'ew': 'red'
              }


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    #   this must hold true, if not it raises exception and program crashes
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

# print(market_2nd)
switch_lights(market_2nd)
# print(market_2nd)
