from django.contrib import admin
from cyoa.models import Choice, Snippet


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['snippet_title','snippet_text']}),
        ('Date', {'fields': ['pub_date']}),
        ('Image & Ending Options', {'fields': ['display_title','ending','display_image','image']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Snippet, SnippetAdmin)

list_display = ('snippet_text', 'pub_date', 'was_published_recently')