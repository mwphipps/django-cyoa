from django.contrib import admin
from django.utils import timezone
from django import forms
from cyoa.models import Story, Snippet, Choice, First
from datetime import date

class SnippetForm(forms.ModelForm):

    is_intro = forms.BooleanField()

    def save(self, commit=True):
        is_intro = self.cleaned_data.get('is_intro', None)
        # ...do something with extra_field here...
        return super(SnippetForm, self).save(commit=commit)

    class Meta:
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
        ('Image & Ending Options', {'fields': ['display_title', 'is_intro', 'ending', 'display_image', 'image']}),
    ]
    list_display = ('id', 'snippet_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    form = SnippetForm
    
admin.site.register(Story, StoryAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(First)


