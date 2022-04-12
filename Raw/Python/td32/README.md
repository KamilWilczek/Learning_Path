regarding episode 34 - Deploy Django to Digital Ocean App Platform - Python & Django 3.2 Tutorial Series
https://www.youtube.com/watch?v=FjWbMNw6Wk0&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL&index=34&ab_channel=CodingEntrepreneurs

"For everyone following this tutorial: make sure there isn't a mismatch between the POSTGRES_USERNAME variable set up in the settings.py file and the environment variable, as Justin pointed out in 44:33. Also, if you have been following along the tutorial and are trying to deploy from your local files, your "home_view" function might take a random integer and query an Article against the database. That might cause some errors after deploying so make sure the query isn't trying to access a register that hasn't been created yet."

#################################################################

home-view:

################################################################
{% extends "base.html" %}

{% block content %}
<h1>{{ object.title }} (id: {{ id }})!</h1>
<p>{{ content }}!</p>

<a href='{% url "articles:create" %}'>Create Article</a>
<a href='{% url "articles:detail" slug="hello-world" %}'>Hello world article</a>
<ul>
    {% for x in object_list %}
        {% if x.title %}
            <li><a href='{{ x.get_absolute_url }}'>{{ x.title }} - {{ x.content }}</a></li>
        {% endif %}
    {% endfor %}
</ul>

{% endblock content %}
####################################################################

views.py:

####################################################################
"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Justin" # hard coded
    random_id = random.randint(1, 4) # pseudo random
    
    # from the database??
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} (id: {id})!</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)
##################################################################################