from django.conf.urls import url

from .views import ChapterDetailView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', ChapterDetailView.as_view(), name='ttip-chapter-detail'),
]
