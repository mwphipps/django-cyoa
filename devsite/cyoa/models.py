from django.db import models
from django.utils import timezone
from django import forms
from datetime import date
import datetime

class Story(models.Model):
	class Meta:
		verbose_name_plural = "stories"
	story_title = models.TextField(max_length=140, default='Title')
	story_beginning_snippet = models.IntegerField(default=0)
	story_author = models.TextField(max_length=140, default='Anonymous')
	story_year =  models.TextField(max_length=42, default=date.today().year)
	story_descript = models.TextField(max_length=2000)
	def __str__(self):              # __unicode__ on Python 2
		return self.story_title
	list_filter = ['story_title']
	search_fields = ['story_title','story_author','story_descript']


class Snippet(models.Model):
    snippet_text = models.TextField(max_length=2000)
    snippet_title = models.TextField(max_length=140, default='Title')
    story = models.ForeignKey(Story)
    ending = models.BooleanField(default=False)
    image = models.TextField(max_length=140, default='No Image')
    display_image = models.BooleanField(default=False)
    display_title = models.BooleanField(default=False)
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

class Choice(models.Model):
    snippet = models.ForeignKey(Snippet)
    choice_text = models.CharField(max_length=250)
    snippet_link = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text

class First(models.Model):
	class Meta:
		verbose_name_plural = "Story Introduction Snippets"
	story = models.ForeignKey(Story)
	snippet = models.ForeignKey(Snippet)
	def __str__(self):              # __unicode__ on Python 2
		return str(self.snippet)
