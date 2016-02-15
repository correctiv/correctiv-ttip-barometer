from django.views.generic.detail import DetailView

from .models import Chapter


class ChapterDetailView(DetailView):

    queryset = Chapter.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        context['object_list'] = Chapter.objects.exclude(id=self.object.pk)
        return context
