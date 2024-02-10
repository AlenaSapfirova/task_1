from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author',
                               on_delete=models.CASCADE,
                               verbose_name='автор')
    header = models.CharField(max_length=200, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    date_created = models.DateField(auto_now_add=True)
    published = models.BooleanField()

    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('author__username', 'header')
