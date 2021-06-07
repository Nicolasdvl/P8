from django.shortcuts import render
from search.search import SearchForm

# Create your views here.


def index(request):
    form = SearchForm()
    return render(request, "core/index.html", {"form": form})
