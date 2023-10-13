from django.db import models

# Create your models here.
class KEYWORD(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class TREND(models.Model):
    name = models.TextField()
    result = models.IntegerField()
    search_period = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)