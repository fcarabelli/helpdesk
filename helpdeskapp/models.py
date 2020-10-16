from django.db import models

# Create your models here.
class Question(models.Model):
    URGENCY = (
        ("HIGH","Alta"),
        ("MEDIUM", "Media"),
        ("LOW","Baja"),
    )
    subject = models.CharField(max_length=72,blank=False)
    message = models.CharField(max_length=1000,blank=False)
    urgency = models.CharField(max_length=10,choices=URGENCY,blank=False)
    question_datetime = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254,blank=False,help_text="Ingresá tu mail de uso frecuente")
