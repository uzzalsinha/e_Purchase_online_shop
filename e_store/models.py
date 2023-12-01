from django.db import models
from collection.models import Collection
from django.urls import reverse


class Product(models.Model):
    product_name    = models.CharField(max_length=100, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    des             = models.TextField(max_length=250, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='images/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Collection, on_delete=models.CASCADE)
    adding_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])