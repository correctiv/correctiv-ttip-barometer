from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Chapter(models.Model):
    STATUS_CHOICES = (
        (0, _('Just started.')),
        (15, _('No agreement in sight.')),
        (30, _('It\'s complicated.')),
        (60, _('There\'s a first contract draft.')),
        (75, _('Agreement in sight.')),
        (100, _('The contract is concluded.')),
    )
    title = models.CharField(max_length=255)
    long_title = models.CharField(max_length=512, default='', blank=True)
    slug = models.SlugField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=15)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    teaser = models.TextField(blank=True)
    image = FilerImageField(blank=True, default=None,
                            null=True, on_delete=models.SET_NULL,
                            verbose_name=_('image'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    body = models.TextField(blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

    @property
    def description(self):
        return self.teaser

    @models.permalink
    def get_absolute_url(self):
        return ('ttip_barometer:ttip-chapter-detail', (), {'slug': self.slug})

    def get_status_text(self):
        if self.published:
            return dict(self.STATUS_CHOICES)[self.status]
        else:
            return _("No barometer yet")

    def get_status_value(self):
        if self.published:
            return self.status
        else:
            return 0

    def get_next(self):
        try:
            return Chapter.objects.filter(order__gt=self.order)[0]
        except IndexError:
            return None

    def get_previous(self):
        try:
            return Chapter.objects.filter(order__lt=self.order).order_by('-order')[0]
        except IndexError:
            return None
