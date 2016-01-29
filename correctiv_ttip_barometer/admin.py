from django.contrib import admin

from .models import Chapter


class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'updated', 'published')

admin.site.register(Chapter, ChapterAdmin)
