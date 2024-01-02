
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reader(models.Model):
    # img = models.ImageField()
    img = models.ImageField(upload_to='posts/media/uploads/', blank = True, null = True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) # ekjon user 12 digit obdi taka rakhte parbe, dui doshomik ghor obdi rakhte parben 1000.50
    user = models.OneToOneField(User, related_name='reader', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


