from audioop import reverse
from distutils.command.upload import upload
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

""" 
Models are like a template to create database table in database.
"""


class Category(models.Model):
    name = models.CharField(_("Category Name") ,max_length=255 , db_index=True)
    slug = models.SlugField(max_length=255 , unique=True)

    '''
    Slug in django is a short label for something , containing
    only letters , numbers , underscores or hyphens.
    They're generally used in URLs(like in django docs).
    A slug field in django is used to store and generate valid
    URLs for your dynamically created web pages.
    '''
    
    class Meta:
        # overwriting name in django db
        verbose_name_plural = 'categories'
    
    # returning name when assigning or sending
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category , related_name='product' , on_delete=models.CASCADE)
    created_by = models.ForeignKey(User , related_name='product_creator' , on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255 , default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',) #odering data in db in descending order
        
    def __str__(self):
        return self.title
    
    
    
    