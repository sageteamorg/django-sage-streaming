from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

class WatchLog(models.Model):
    """Stream watch log"""
    video_path = models.CharField(
        _('Video Path'),
        max_length=255
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='watch_logs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_authenticated = models.BooleanField(
        _('Is Authenticated'),
        default=False
    )

    ip = models.GenericIPAddressField(
        _('IP Address'),
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Created At'),
        auto_now_add=True
    )

    def __str__(self):
        return f'Watch Log ip: {self.ip}, created at {self.created}'

    class Meta:
        verbose_name = _('Watch Log')
        verbose_name_plural = _('Watch Logs')
        ordering = ('-created',)
