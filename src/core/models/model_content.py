from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _


class SectionContent(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))

    # Translated fields
    title_translated = models.JSONField(
        _('Translated Title'), blank=True, null=True)
    description_translated = models.JSONField(
        _('Translated Description'), blank=True, null=True)

    def __str__(self):
        return f"{self.content_type} - {self.object_id}"

    class Meta:
        verbose_name = _('Section Content')
        verbose_name_plural = _('Section Contents')
