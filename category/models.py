from distutils.command.upload import upload
from django.db import models
from django.urls import reverse


class Category(models.Model):
    # category_name slug description cat_image
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    # !!! no need '.' if href="{% url 'products_by_category' category.slug %}" !!!
    #                 ------------------------------------------------------------

    def __str__(self):
        return self.category_name
