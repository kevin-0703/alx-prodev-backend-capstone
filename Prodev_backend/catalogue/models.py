from django.db import models
from django.utils.text import slugify
# Create your models here.




class Category(models.Model):
   name = models.CharField(max_length=100, unique=True)
   slug = models.SlugField(max_length=120, unique=True)


   class Meta:
       ordering = ['name']


   def save(self, *args, **kwargs):
       if not self.slug:
          self.slug = slugify(self.name)
       return super().save(*args, **kwargs)


   def __str__(self):
       return self.name


class Product(models.Model):
   sku = models.CharField(max_length=64, unique=True)
   title = models.CharField(max_length=255)
   slug = models.SlugField(max_length=255, unique=True)
   description = models.TextField(blank=True)
   price = models.DecimalField(max_digits=12, decimal_places=2, db_index=True)
   available = models.BooleanField(default=True, db_index=True)
   category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   inventory = models.IntegerField(default=0, db_index=True)


   class Meta:
       ordering = ['-created_at']
       indexes = [
       models.Index(fields=['sku']),
       models.Index(fields=['price']),
       models.Index(fields=['available', 'category']),
     ]


   def __str__(self):
      return self.title