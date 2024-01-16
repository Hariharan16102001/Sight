from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import destruction
from django.shortcuts import render

def index(request):
    all_books = destruction.objects.all()
    context = {
        'all_books' : all_books
    }

    return render(request,'destruction/index.html',context)

def detail(request,book_id):
    return HttpResponse("<h>This is book id : " + str(book_id) + "</h>")