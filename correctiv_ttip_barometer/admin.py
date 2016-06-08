from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin
from pagedown.widgets import AdminPagedownWidget
from parler.admin import TranslatableModelForm, TranslatableStackedInline

from correctiv_community.helpers.i18n import CustomTranslatableAdmin

from .models import Chapter, ChapterDocument


class ChapterDocumentInlineAdmin(TranslatableStackedInline, admin.StackedInline):
    model = ChapterDocument
    extra = 0

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('title',)
        }


class ChapterAdminForm(TranslatableModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
        widgets = {
            'body': AdminPagedownWidget
        }


class ChapterAdmin(SortableAdminMixin, CustomTranslatableAdmin):
    form = ChapterAdminForm
    inlines = [
        ChapterDocumentInlineAdmin
    ]

    list_display = ('title', 'updated', 'published')

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('title',)
        }

admin.site.register(Chapter, ChapterAdmin)
