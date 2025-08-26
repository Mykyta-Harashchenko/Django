from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
import random

from core.quotes.models import Quote, Author, Tag
from core.quotes.utils import get_mongodb
from core.quotes.forms import AuthorForm, QuoteForm, TagForm


# Create your views here.
def main(request, page=1):
    sort_by = request.GET.get('sort_by', 'created_at')

    sort_by = request.GET.get('sort_by', 'created_at_desc')

    if sort_by == 'created_at_asc':
        quotes = Quote.objects.all().order_by('created_at')
    elif sort_by == 'created_at_desc':
        quotes = Quote.objects.all().order_by('-created_at')
    elif sort_by == 'likes':
        quotes = Quote.objects.all().order_by('-likes')
    elif sort_by == 'quote':
        quotes = Quote.objects.all().order_by('quote')
    else:
        quotes = Quote.objects.all().order_by('-created_at')
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
            return render(
                request,
                'quotes/add_quote.html',
                {'form': form},
                status=400
            )
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def search_quotes(request):
    query = request.GET.get('q')
    if query:
        # Поиск по содержимому цитаты и автору
        quotes = Quote.objects.filter(quote__icontains=query) | Quote.objects.filter(author__fullname__icontains=query)
    else:
        quotes = Quote.objects.all()
    return render(request, 'quotes/search_results.html', {'quotes': quotes})


def random_quote(request):
    quote = random.choice(Quote.objects.all())

    return render(request, 'quotes/random_quote.html', {'quote': quote})

def like_quote(request, quote_id):
    if request.method == "POST":
        quote = get_object_or_404(Quote, id=quote_id)
        quote.likes += 1
        quote.save()
        return JsonResponse({'likes': quote.likes})


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