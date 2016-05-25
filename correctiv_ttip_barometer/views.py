from django.views.generic.detail import DetailView

from parler.views import TranslatableSlugMixin

from .models import Chapter


class ChapterDetailView(TranslatableSlugMixin, DetailView):

    queryset = Chapter.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        published_objects = Chapter.objects.filter(published=True)
        context['object_list'] = published_objects.exclude(id=self.object.pk)
        return context


class ChapterDocumentDetailView(TranslatableSlugMixin, DetailView):
    template_name = 'correctiv_ttip_barometer/chapter_document.html'
    queryset = Chapter.objects.filter(published=True, document__isnull=False)
