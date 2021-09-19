from django.db import models
from django.utils import timezone

from article.models import Article
from user_info.models import User


class Collect(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='collections'
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='collections'
    )
    has_collect = models.BooleanField(default=1)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{}_{}".format(self.author.username, self.article)

