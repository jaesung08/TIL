from django.db import models

class TestModel(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    genre = models.CharField(max_length=20)
    score = models.FloatField()
