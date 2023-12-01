from django.db import models
from django.urls import reverse

# Create your models here.

class Collection(models.Model):
    collection_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=250, blank=True)
    collection_img = models.ImageField(upload_to='images/collections', blank=True)

    class Meta:
        verbose_name = 'collection'
        verbose_name_plural = 'collections'
    def get_url(self):
        return reverse('products_by_collection', args=[self.slug])
    def __str__(self):
        return self.collection_name