#from django.db import models

# # Create your models here.
# from django.db import models

# class Usuário(models.Model):
#     nome = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=100, unique=True)
#     avatar = models.CharField(max_length=255, null=True)

#     def __str__(self):
#         return self.nickname

# class Questionário(models.Model):
#     titulo = models.CharField(max_length=100)
#     descricao = models.CharField(max_length=500, null=True)
#     data_criacao = models.DateTimeField(auto_now_add=True)
#     questionario_col = models.CharField(max_length=45, null=True)
#     capa = models.CharField(max_length=255, null=True)
#     usuário = models.ForeignKey(Usuário, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.titulo

# class Hashtag(models.Model):
#     tag = models.CharField(max_length=45, unique=True)

#     def __str__(self):
#         return self.tag

# class Hashtag_has_questionário(models.Model):
#     hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
#     questionário = models.ForeignKey(Questionário, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('hashtag', 'questionário')

from ast import Import
from time import timezone
from django.db import models
import datetime 
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text