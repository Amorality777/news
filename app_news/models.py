from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey('StatusNews', default=None, null=True, on_delete=models.CASCADE, related_name='news')

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'News'

    def get_absolute_url(self):
        return reverse('news_create')


class Comments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, null=True, related_name='comments')
    username = models.CharField(max_length=20)
    comment = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey('News', default=None, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['news', '-date']


class StatusNews(models.Model):
    status = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'StatusNews'
        db_table = 'status_news'
