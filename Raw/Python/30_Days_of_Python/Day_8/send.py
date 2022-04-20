# built-in modules
import sys
import requests
from datetime import datetime

# own modules
from formatting import format_msg


def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website)
        # send the message
        r = requests.get("http://httpbin.org/json")
        if r.status_code == 200:
            return r.json()
        else:
            return "There was an error"


# to run just after opening file
# response = send("Justin", verbose=True)
# print(response)

# pythonic way to run script from cli so functions run
if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, verbose=True)
    print(response)


# examples of built-in functions without imports
# format()
# str()
# int()

"""
python
from datetime import datetime
datetime.now()
datetime.now()
datetime.now()
exit()
"""

"""
python -i send.py
send()
send('Justin')
exit()
"""

"""
pip install requests
import requests
requests.get()
from requests import get
requests.get("http://httpbin.org")
r = requests.get("http://httpbin.org/json")
print(r.json)
r.status_code
exit()
"""

"""
python -i send.py
send()
send('Justin')
exit()
"""
