from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import get_language

from filer.fields.image import FilerImageField
from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language


def document_path(instance, filename):
    return 'investigations/ttip/leak/chapters/{0}.pdf'.format(instance.slug)


@python_2_unicode_compatible
class Chapter(TranslatableModel):
    STATUS_CHOICES = (
        (0, _('Just started.')),
        (15, _('No agreement in sight.')),
        (30, _('It\'s complicated.')),
        (60, _('There\'s a first contract draft.')),
        (75, _('Agreement in sight.')),
        (100, _('The contract is concluded.')),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=15)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    image = FilerImageField(blank=True, default=None,
                            null=True, on_delete=models.SET_NULL,
                            verbose_name=_('image'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    published = models.BooleanField(default=False)

    document = models.FileField(upload_to=document_path, blank=True, null=True)

    translations = TranslatedFields(
          title=models.CharField(max_length=255),
          slug=models.SlugField(),
          long_title=models.CharField(max_length=512),
          teaser=models.TextField(blank=True),
          body=models.TextField(blank=True),
    )

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

    @property
    def description(self):
        return self.teaser

    @models.permalink
    def get_absolute_url(self):
        with switch_language(self, get_language()):
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
