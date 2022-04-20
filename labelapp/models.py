from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    passswd = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.username

class Label(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    label_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.label_text

    

