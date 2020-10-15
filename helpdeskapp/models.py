from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=72,blank=False)
    message = models.CharField(max_length=1000,blank=False)
    question_datetime = models.DateTimeField(auto_now=True)