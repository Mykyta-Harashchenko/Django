import pytest
from core.quotes.models import Quote, Tag, Author
from datetime import datetime

timestamp = datetime.now()

@pytest.mark.django_db
def test_create_quote():
    author = Author.objects.create(fullname='Test author', born_date="1 January 1990", born_location='Vienna, Austria', created_at=timestamp, description='iuehdadsofnosdnfoksdkfnsldkfnlk')
    quote = Quote.objects.create(quote="Test quote", author=author, created_at=timestamp)
    tag = Tag.objects.create(name='Test tag')
    assert tag.name == "Test tag"
    assert quote.quote == "Test quote"
    assert author.fullname == "Test author"