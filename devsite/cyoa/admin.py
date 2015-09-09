from django.contrib import admin
from cyoa.models import Story, Snippet, Choice

class StoryAdmin(admin.ModelAdmin):
    fieldsets = [
         (None,               {'fields': ['story_title']}),
    ]


class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['snippet_title','snippet_text']}),
        ('Date', {'fields': ['pub_date']}),
        ('Image & Ending Options', {'fields': ['display_title', 'ending','display_image','image']}),
    ]
#    inlines = [ChoiceInline]


admin.site.register(Story, StoryAdmin)
admin.site.register(Snippet, SnippetAdmin)


list_display = ('snippet_text', 'pub_date', 'was_published_recently')