from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    discription  = models.TextField()
    auther = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=3 , decimal_places=2)
    cover = models.ImageField(upload_to='covers/' , blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse ('book_detail' ,args=[self.id] )

class Comment (models.Model):
    user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book=models.ForeignKey(Book , on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} :{self.text}'
