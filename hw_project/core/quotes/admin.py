from django import forms
from django.contrib import admin

from core.quotes.models import Quote, Author, Tag

# Register your models here.

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'rows':4, 'cols':60}),
        }
        
class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 1


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    form = QuoteForm
    list_display = ('quote', 'author', 'created_at', 'likes')
    search_fields = ('quote', 'author__fullname', 'tag_name')
    ordering = ('-created_at',)
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [QuoteInline]
    list_display = ('fullname', 'born_date', 'born_location', 'description', 'created_at')
    search_fields = ('fullname', 'quote__quote')
    ordering = ('-created_at',)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)