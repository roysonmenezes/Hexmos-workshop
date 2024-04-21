import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
# class Question(models.Model):
#     question_text=models.CharField(max_length=200)
#     pub_date=models.DateTimeField("date published on")

#     def __str__(self):
#         return self.question_text
    
#     @admin.display(
#         boolean=True,
#         ordering="pub_date",
#         description="Published recently?",
#     )
    
#     def was_published_recently(self):
#         now=timezone.now()
#         return now-datetime.timedelta(days=1) <= self.pub_date <= now
   

# class Choice(models.Model):
#     question=models.ForeignKey(Question,on_delete=models.CASCADE)
#     choice_text=models.CharField(max_length=200)
#     votes=models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text
    
#week 4
class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
    
class OptionVote(models.Model):  # Change class name to OptionVote
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option_text

class Tags(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tag_name