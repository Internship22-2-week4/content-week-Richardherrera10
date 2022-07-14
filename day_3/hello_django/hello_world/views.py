from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  # print(request.data.get('name'))
  return HttpResponse("Hello, world!")