from django.views.generic.detail import DetailView

from .models import Chapter


class ChapterDetailView(DetailView):

    queryset = Chapter.objects.filter(published=True)
