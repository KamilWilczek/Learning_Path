"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sedns request)
    Return HTML as a response (We pick to return the response)
    """

    name = "Justin"  # hard coded
    random_id = random.randint(1, 4)  # pseudo random

    # from the database??
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }

    # Django templates
    # tmpl = get_template('home-view.html')
    # tmpl_string = tmpl.render(context=context)

    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>Hello {title} (id: {id})!</h1>
    # <p>Hi {content}!</p>
    # """.format(
    #     **context
    # )

    return HttpResponse(HTML_STRING)
