from django.urls import URLPattern, path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('author/<int:author_id>', views.author, name='author'),
  path('category/<int:category_id>', views.category, name='category'),

]
