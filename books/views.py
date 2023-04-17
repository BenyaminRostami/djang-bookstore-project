from django.views import generic
from .models import Book
from django.urls import reverse_lazy
class BookListViews(generic.ListView) :
    model = Book
    paginate_by = 6
    template_name = 'books/book_list.html'
    context_object_name = 'books'
# Create your views here.
class BookDetailView(generic.DetailView):
    model=Book

    template_name = 'books/book_detail.html'
class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title' , 'discription' , 'auther' , 'price', 'cover']
    template_name = 'books/book_create.html'
class BookUpdateView(generic.UpdateView) :
    model = Book
    fields = ['title' , 'auther' , 'discription' , 'price'  , 'cover']
    template_name = 'books/book_update.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy ('book_list')