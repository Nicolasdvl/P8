"""
Django views for authentification app.

Python functions that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect,
or a 404 error, or an XML document, or an image . . .
"""
from django.shortcuts import render
from search.search import SearchForm


def index(request):
    """Render 'index.html'."""
    search_form = SearchForm()
    return render(request, "core/index.html", {"SearchForm": search_form})

def legal(request):
    """Render 'legal_notice.html'."""
    return render(request, "core/legal_notice.html")
