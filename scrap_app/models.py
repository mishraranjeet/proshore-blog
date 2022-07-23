from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    blog_image_url = models.URLField(blank=True, null=True)
    author_name = models.CharField(max_length=500, null=True, blank=True)
    author_image_url = models.URLField(blank=True, null=True)
    designation = models.CharField(max_length=500, null=True, blank=True)
    reading_time = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "blog"

