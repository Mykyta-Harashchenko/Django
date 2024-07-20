from django import forms
from .models import Quote, Author, Tag


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    quote =forms.CharField(min_length=10, widget=forms.Textarea(attrs={'rows': 3}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select())
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']


class TagForm(forms.ModelForm):
    name = forms.CharField(min_length=3, max_length=25, required=True, widget=forms.TextInput())

    class Meta:
        model = Tag
        fields = ['name']
