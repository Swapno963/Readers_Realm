from django.contrib import admin
from .models import Books,CommentModel
# Register your models here.
admin.site.register(Books)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'commentor', 'books_comment', 'body', 'created_on')
    list_filter = ('books_comment', 'created_on')
    search_fields = ('name', 'commentor__username', 'body')

admin.site.register(CommentModel, CommentModelAdmin)