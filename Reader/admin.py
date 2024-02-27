from django.contrib import admin
from .models import Reader,Borrow_model
# Register your models here.
admin.site.register(Reader)

class BorrowModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'purchase_date', 'book', 'IsBorrowed')
    list_filter = ('IsBorrowed', 'purchase_date')
    search_fields = ('user__username', 'book__title')

admin.site.register(Borrow_model, BorrowModelAdmin)