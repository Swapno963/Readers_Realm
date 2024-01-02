from django.contrib import admin
from .models import Books,CommentModel
# Register your models here.
admin.site.register(Books)
admin.site.register(CommentModel)