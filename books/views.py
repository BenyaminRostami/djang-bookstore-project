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