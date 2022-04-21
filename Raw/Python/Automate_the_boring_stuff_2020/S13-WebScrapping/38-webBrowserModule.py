import webbrowser
import sys
import pyperclip

# print(webbrowser.open('https://automatetheboringstuff.com'))

# check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St. San Francisco'
    # Wieniec 1
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.pl/maps/search/<ADDRESS>
webbrowser.open('https://www.google.pl/maps/search/' + address)


