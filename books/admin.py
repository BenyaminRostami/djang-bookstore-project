from django.contrib import admin
from .models import *
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user" , "book" , "text" , "datetime_created")
# Register your models here.
admin.site.register(Book)
admin.site.register(Comment,CommentAdmin)