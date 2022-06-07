from unittest import result
from django.db.models.deletion import CASCADE
from quizes.models import Quiz
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

    
User=get_user_model()   

class Result(models.Model):
        quiz = models.ForeignKey(Quiz, on_delete= models.CASCADE)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
        score = models.FloatField()

        def __str__(self):
                return str(self.user)
    