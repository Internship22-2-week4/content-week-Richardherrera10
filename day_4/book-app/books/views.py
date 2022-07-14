from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, Category
# Create your views here.
def index(request):
  books = Book.objects.all()
  for book in books:
    print(book.title, book.author.first_name, book.category.name)
  return render(request, 'books/index.html', {
    "booklists": books
  })
  # return HttpResponse('App book')

def author(request, author_id):
  author = Author.objects.get(id=author_id)
  return render(request, 'books/author.html',{
    "author": author
  })
 # return HttpResponse(f'<h1>Author id:{author_id}</h1>')

def category(request, category_id):
  return HttpResponse(f'category id:{category_id}')