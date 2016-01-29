from django.contrib import admin

from .models import Chapter


class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Chapter)
