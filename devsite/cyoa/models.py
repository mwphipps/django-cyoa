from django.db import models
from django.utils import timezone
from django import forms

class Story(models.Model):
    story_text = models.TextField(max_length=2000)
    story_title = models.TextField(max_length=42, default='Title')
    ending = models.IntegerField(default=0)
    image = models.TextField(max_length=42, default='No Image')
    display_image = models.IntegerField(default=0)
    display_title = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.story_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    list_filter = ['pub_date']
    search_fields = ['story_title','story_text']

class Choice(models.Model):
    story = models.ForeignKey(Story)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    story_link = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text