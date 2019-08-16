from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class userlogin(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=15)
    password2 =models.CharField(max_length=15)
    class Meta:
        db_table='userlogin'


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
# class Trail1(AbstractUser):
#     email = models.CharField(max_length=15)
#     class Meta:
#         db_table='userlogin'


