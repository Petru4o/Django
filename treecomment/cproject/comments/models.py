from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField()
    comments = GenericRelation('comment')

    def __str__(self):
        return self.title



class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    parent = models.ForeignKey(
        'self',
        verbose_name='Parent comment',
        blank=True,
        null=True,
        related_name='comment_children',
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Date of creating')

    def __str__(self):
        return str(self.id)
