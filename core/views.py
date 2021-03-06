"""
Django views for authentification app.

Python functions that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect,
or a 404 error, or an XML document, or an image . . .
"""
from django.shortcuts import render
from search.search import SearchForm


def index(request):
    """Render index.html."""
    form = SearchForm()
    return render(request, "core/index.html", {"form": form})
