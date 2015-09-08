from django.contrib import admin
from cyoa.models import Choice, Story


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class StoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['story_title','story_text']}),
        ('Date', {'fields': ['pub_date']}),
        ('Image & Ending Options', {'fields': ['display_title','ending','display_image','image']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Story, StoryAdmin)

list_display = ('story_text', 'pub_date', 'was_published_recently')