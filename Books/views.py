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
from rest_framework import filters, pagination
# from .models import 
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def show_all_books(request, category_slug=None):
    user = request.user
    book_list = Books.objects.all()
    categori_list = Category.objects.all()

    if category_slug:
        category_type = Category.objects.filter(slug=category_slug).first()
        if category_type:
            book_list = Books.objects.filter(category = category_type)
    

    # new code start
            # Get the page number from the GET request (default to 1)
    page = request.GET.get('page', 1)

    # Create the Paginator object with desired number of items per page
    paginator = Paginator(book_list, 2)  # Adjust `10` as needed

    # Try to get the requested page object, handle invalid page numbers
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    # Pass the paginated books, categories, user, and other context data
    context = {
        'page_obj': page_obj,
        'category_list': categori_list,
        'user': user,
        # Add any other context data needed for your template
    }

    return render(request, 'book_list.html', context)
    # new code end

    # return render(request,'book_list.html',{'book_list':book_list, 'category_list':categori_list,'user':user}) 


class ShowDetailBook(DetailView):
    model = Books
    template_name = 'detail.html'
    context_object_name = 'Books'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        book_list = self.get_object()
        comments = book_list.comments.all()
        print(book_list)
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
   