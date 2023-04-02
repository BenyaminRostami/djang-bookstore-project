from django.urls import path
from .views import *
urlpatterns= [
    path ('',BookListViews.as_view() , name = 'book_list') ,
    path('<int:pk>/' ,BookDetailView.as_view() , name = "book_detail"),
    path ('create/' , BookCreateView.as_view() , name= "book_create"),
    path("<int:pk>/edit/" , BookUpdateView.as_view() , name="book_update")

]