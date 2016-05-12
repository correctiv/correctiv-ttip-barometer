from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import ChapterDetailView, ChapterDocumentDetailView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', ChapterDetailView.as_view(), name='ttip-chapter-detail'),
    url(_(r'^(?P<slug>[\w-]+)/documents/$'), ChapterDocumentDetailView.as_view(), name='ttip-chapterdocument-detail'),
]
