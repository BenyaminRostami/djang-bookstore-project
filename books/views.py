from django.views import generic
from .models import Book
class BookListViews(generic.ListView) :
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
# Create your views here.
class BookDetailView(generic.DetailView):
    model=Book
    template_name = 'books/book_detail.html'
class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title' , 'discription' , 'auther' , 'price']
    template_name = 'books/book_create.html'
class BookUpdateView(generic.UpdateView) :
    model = Book
    fields = ['title' , 'auther' , 'discription' , 'price']
    template_name = 'books/book_update.html'

