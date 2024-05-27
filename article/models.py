from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='article/')
    read_time = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
