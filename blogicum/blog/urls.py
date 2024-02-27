from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Если вызван URL без относительного адреса (шаблон — пустые кавычки),
    # то вызывается view-функция index() из файла views.py
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.category_post, name='category_post')
]
