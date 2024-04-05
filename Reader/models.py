from django.db import models
from django.contrib.auth.models import User
from Books.models import Books

# Create your models here.
class Reader(models.Model):
    user = models.OneToOneField(User, related_name='reader', on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) # ekjon user 12 digit obdi taka rakhte parbe, dui doshomik ghor obdi rakhte parben 1000.50
    email =models.EmailField(null=True, blank=True)
    # image = models.ImageField(upload_to='reader_images/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}"



class Borrow_model(models.Model):
    user = models.ForeignKey(Reader, on_delete=models.CASCADE,null=True,blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE,null=True,blank=True)
    IsBorrowed = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.user }-"    