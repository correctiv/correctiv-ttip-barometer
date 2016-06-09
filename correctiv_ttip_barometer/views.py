from django.views.generic.detail import DetailView
from django.shortcuts import Http404

from parler.views import TranslatableSlugMixin

from .models import Chapter, ChapterDocument


class ChapterDetailView(TranslatableSlugMixin, DetailView):

    queryset = Chapter.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        published_objects = Chapter.objects.filter(published=True)
        context['object_list'] = published_objects.exclude(id=self.object.pk)
        return context


class ChapterDocumentDetailView(TranslatableSlugMixin, DetailView):
    template_name = 'correctiv_ttip_barometer/chapter_document.html'
    queryset = Chapter.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ChapterDocumentDetailView, self).get_context_data(**kwargs)
        document_id = self.kwargs.get('document_id', None)

        documents = self.object.chapterdocument_set.all()
        document = None

        if document_id is not None:
            try:
                document = self.object.chapterdocument_set.get(pk=int(document_id))
            except ChapterDocument.DoesNotExist:
                raise Http404()

        if document is None and documents:
            document = documents[0]

        context['documents'] = documents
        context['document'] = document
        return context
