from django.db import models
from datetime import  date
from django.contrib.auth.models import User

# Create your models here.
class Todowoorks(models.Model):
    workname=models.CharField(max_length=120)
    date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    fileupload=models.FileField(blank=True)

    def get_self_id(self):
        return self.id