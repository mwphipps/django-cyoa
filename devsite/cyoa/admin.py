from django.contrib import admin
from django.utils import timezone
from django import forms
import requests
from cyoa.models import Story, Snippet, Choice, First
from datetime import date


class SnippetForm(forms.ModelForm):
    model = Snippet	
    exclude = []

class StoryAdmin(admin.ModelAdmin):
    fieldsets = [
         (None,               {'fields': ['story_title', 'story_author', 'story_year', 'story_descript',]}),
    ]
    list_display = ('story_title', 'story_author', 'story_year')

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['snippet_title','snippet_text']}),
        ('Date', {'fields': ['pub_date']}),
        ('Story Selection', {'fields': ['story']}),
        ('Image & Ending Options', {'fields': ['display_title', 'ending', 'display_image', 'image']}),
    ]
    list_display = ('id', 'snippet_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    form = SnippetForm
    
admin.site.register(Story, StoryAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(First)


