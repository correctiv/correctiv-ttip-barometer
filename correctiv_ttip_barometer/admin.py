from django.contrib import admin
from django import forms

from adminsortable2.admin import SortableAdminMixin
from pagedown.widgets import AdminPagedownWidget

from .models import Chapter


class ChapterAdminForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
        widgets = {
            'body': AdminPagedownWidget
        }


class ChapterAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = ChapterAdminForm

    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'updated', 'published')

admin.site.register(Chapter, ChapterAdmin)
