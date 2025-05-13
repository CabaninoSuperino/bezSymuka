from django.shortcuts import get_object_or_404, render
from .models import Author
from .models import Book

def index(request):
    authors = Author.objects.all()
    return render(request, 'polls/index.html', {'author_list': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'polls/author_detail.html', {'author': author})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "polls/book_detail.html", {"book": book})



def book_price(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'polls/book_price.html', {'book': book})
