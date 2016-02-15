from django.views.generic.detail import DetailView

from .models import Chapter


class ChapterDetailView(DetailView):

    queryset = Chapter.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        publishedObjects = Chapter.objects.filter(published=True)
        context['object_list'] = publishedObjects.exclude(id=self.object.pk)
        return context
