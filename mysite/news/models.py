from django.db import models

class News(models.Model):
    name = models.CharField(max_length=150)

