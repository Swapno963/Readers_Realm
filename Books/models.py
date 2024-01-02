from django.db import models
from Reader.models import Reader
from Category.models import Category
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='posts/media/uploads/', blank = True, null = True)    
    borrow_price = models.IntegerField()
    book_borrower = models.ForeignKey(Reader, related_name='book_borrower', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self) -> str:
        return f"{self.title}-{self.borrow_price}"
    


class CommentModel(models.Model):
    name = models.CharField(max_length=30)
    books_comment = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
        return f"{self.name}-{self.created_on}"
    