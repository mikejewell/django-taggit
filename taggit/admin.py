from __future__ import unicode_literals

from django.contrib import admin

from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem

class TagAdmin(admin.ModelAdmin):
    list_display = ["name","slug"]
    search_fields = ('name','slug')
    inlines = [
        TaggedItemInline
    ]
    ordering = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Tag, TagAdmin)
admin.site.register(TaggedItem)
