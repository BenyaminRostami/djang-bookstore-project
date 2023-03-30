from django.db import models
from django.urls import reverse
# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    discription  = models.TextField()
    auther = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=3 , decimal_places=2)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse ('book_detail' ,args=[self.id] )


