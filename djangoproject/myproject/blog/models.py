from django.db import models
from datetime import datetime
from users.models import Adduser

# Create your models here.
class Blogadd(models.Model):
    author = models.ForeignKey(to=Adduser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    blog = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return f"{self.author}"
