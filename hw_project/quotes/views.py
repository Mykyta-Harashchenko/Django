from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Quote, Author, Tag
from .utils import get_mongodb
from .forms import AuthorForm, QuoteForm


# Create your views here.
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # перенаправлення на список цитат
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_list')  # перенаправлення на список цитат
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})


