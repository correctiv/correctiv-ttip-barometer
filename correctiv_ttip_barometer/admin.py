from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Chapter


class ChapterAdmin(SortableAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'updated', 'published')

admin.site.register(Chapter, ChapterAdmin)
