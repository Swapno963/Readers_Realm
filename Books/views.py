from .models import Books, CommentModel
from Category.models import Category
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Books
from .forms import CommentForm
from Reader.models import Borrow_model

from django.shortcuts import get_object_or_404, redirect

from django.utils.encoding import force_str
from django.contrib.auth.models import AnonymousUser
from Reader.models import Reader,Borrow_model
# from .models import 



def show_all_books(request, category_slug=None):
    book_list = Books.objects.all()
    categori_list = Category.objects.all()
    if category_slug:
        category_type = Category.objects.filter(slug=category_slug).first()
        if category_type:
            book_list = Books.objects.filter(category = category_type)
    return render(request,'book_list.html',{'book_list':book_list, 'category_list':categori_list}) 


class ShowDetailBook(DetailView):
    model = Books
    template_name = 'detail.html'
    context_object_name = 'Books'
    pk_url_kwarg = 'id'

    # def get(self,request,id,*args, **kwargs):
    #     print('print from books :', id)
    #     return self.get(request,id, *args, **kwargs)


    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        book_list = self.get_object()
        comments = book_list.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['books_comment'] = book_list.title
        context['comment_form'] = comment_form
        return context
    

    def post(self,request, *args, **kwargs):
        print('book post: ',request)
        comment_form = CommentForm(data=self.request.POST)
        book = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=True)
            new_comment.post_book = book
            new_comment.books_comment = book
            new_comment.save()


        return self.get(request,id, *args, **kwargs)
   