from django.db import models

class Question(models.Model):
    question_header = models.CharField(max_length = 50)
    question_text = models.CharField(max_length = 200)
    question_index = models.IntegerField(primary_key=True)
    user_rating = models.IntegerField(default = 0)
    answer_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.question_text

# Create your models here.
