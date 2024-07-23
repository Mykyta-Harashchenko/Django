from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Quote, Author, Tag
from .utils import get_mongodb
from .forms import AuthorForm, QuoteForm, TagForm


# Create your views here.
def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            # db = get_mongodb()
            # authors_collection = db.authors  # Змініть на ім'я вашої колекції
            #
            # author_data = {
            #     "fullname": form.cleaned_data['fullname'],
            #     "born_date": form.cleaned_data['born_date'],
            #     "born_location": form.cleaned_data['born_location'],
            #     "description": form.cleaned_data['description']
            # }
            #
            # authors_collection.insert_one(author_data)
            return redirect(reverse('quotes:root'))
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            # db = get_mongodb()
            # quotes_collection = db.quotes
            #
            # quote_data = {
            #     "quote": form.cleaned_data['quote'],
            #     "tags": form.cleaned_data['tags'],
            #     "author": form.cleaned_data['author'],
            # }
            #
            # quotes_collection.insert_one(quote_data)
            return redirect(reverse('quotes:root'))
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('quotes:root'))
    else:
        form = TagForm()
    return render(request, 'quotes/add_tag.html', {'form': form})

def author_info(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author_info.html', {'author': author})

def quotes_by_tag(request, tag_id, page = 1):
    tag = Tag.objects.get(id=tag_id)
    quotes = Quote.objects.filter(tags=tag)
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})