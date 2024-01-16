from django.db import models

class destruction(models.Model):
    name=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    price=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
