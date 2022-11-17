from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    # get all books from database
    books = Book.objects.all().order_by("title") #order list of books by field/fields in this case title (this is asc -title is desc)
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) # rating__avg if ther is Min("rating") then we would have rating__min
    return render(request, "book_outlet/index.html",{
        "books" : books,
        "total_number_of_books":num_books,
        "average_rating": avg_rating
    })

def book_detail(request, slug):
    # pk = id means primary key equals id to retrieve by book by id
    #try:
    #    book = Book.objects.get(pk=id)
    #except:
    #    raise Http404()
    # helper function which is implemented and does the same as the comment try/except above
    book = get_object_or_404(Book, slug=slug)

    return render(request, "book_outlet/book_detail.html",{
        "title" : book.title,
        "author" : book.author,
        "rating" : book.rating,
        "is_bestselling" : book.is_bestselling
    })
