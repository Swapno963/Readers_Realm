from django.db import models
from Category.models import Category
# Create your models here.'
from django.contrib.auth.models import User
class Books(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='posts/media/uploads/', blank = True, null = True)    
    borrow_price = models.IntegerField()
    book_borrower = ''
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self) -> str:
        return f"{self.title}-{self.borrow_price}"
    


class CommentModel(models.Model):
    commentor = models.OneToOneField(User, related_name='commentor', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)

    books_comment = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
        return f"{self.name}-{self.created_on}"
    
    def save(self, *args, **kwargs):
        if not self.pk and self.commentor is None:
            # If it's a new comment and commentor is not set
            print(self)
        super().save(*args, **kwargs)

