# Core Django imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Third party app imports
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


class Photo(models.Model):

    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField()
    location = models.CharField(max_length=250, null=True, blank=True)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Photo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:photo_detail', kwargs={'title': self.title.lower(), 'slug': self.slug})

