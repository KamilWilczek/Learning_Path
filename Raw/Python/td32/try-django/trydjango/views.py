"""
To render html web pages
"""
import random
from django.http import HttpResponse


def home_view(request):
    """
    Take in a request (Django sedns request)
    Return HTML as a response (We pick to return the response)
    """

    name = "Justin"
    number = random.randint(
        10, 1233123
    )  # API call to some rest API with python & python requests
    H1_STRING = f"""
    <h1>Hello {name} - {number}!</h1>
    """

    P_STRING = f"""<p>Hi {name} - {number}!</p>"""

    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)
