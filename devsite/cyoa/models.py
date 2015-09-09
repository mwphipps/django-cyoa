from django.db import models
from django.utils import timezone
from django import forms

class Snippet(models.Model):
    snippet_text = models.TextField(max_length=2000)
    snippet_title = models.TextField(max_length=42, default='Title')
    beginning = models.IntegerField(default=0)
    ending = models.IntegerField(default=0)
    image = models.TextField(max_length=42, default='No Image')
    display_image = models.IntegerField(default=0)
    display_title = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.snippet_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    list_filter = ['pub_date']
    search_fields = ['snippet_title','snippet_text']


class Stories(models.Model):
	story_title = models.TextField(max_length=42, default='Title')
	snippets = models.ForeignKey(related_name="stories_snippet", Snippet)


class Choice(models.Model):
    snippet = models.ForeignKey(Snippet)
    choice_text = models.CharField(max_length=250)
    snippet_link = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text