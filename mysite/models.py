from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)#博客的标题
    slug = models.CharField(max_length=200)#博客文章的网址
    body = models.TextField()#博客文章的内容
    pub_date = models.DateTimeField(default=timezone.now())#发布时间

    class Meta:
        ordering = ('-pub_date',)
    def __unicode__(self):
        return self.title

