from django.db import models

# Create your models here.


class Gallery(models.Model):
    image = models.ImageField(
        upload_to="uploads/images", null=True, blank=True)
    title = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
