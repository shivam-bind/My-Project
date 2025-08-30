
# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    
class BlogSubSection(models.Model):
    blog = models.ForeignKey(Post, related_name="subsections", on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=200)
    sub_content = models.TextField()

    def __str__(self):
        return f"{self.sub_title} ({self.blog.title})"