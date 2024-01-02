from django.urls import path
from .views import show_all_books, ShowDetailBook


urlpatterns = [
    path('all_books/',show_all_books, name='all_books'),
    path('detail/<int:id>/',ShowDetailBook.as_view(), name='book_detail'),
    path('comment/<int:id>/',ShowDetailBook.as_view(), name='comment_detail'),
    path('category_wise_bookks/<slug:category_slug>/',show_all_books, name='category_wise_book'),
]
