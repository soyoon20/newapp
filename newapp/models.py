from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 저자(글쓴이): author

class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    # 계정이 삭제되면 계정과 연결된 Question 테이블 데이터를 모두 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.subject

class Answer(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   content2 = models.TextField()
   create_date2 = models.DateTimeField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   modify_date = models.DateTimeField(null=True, blank=True)

   def __str__(self):
       return self.content2

    # def __str__(self):
    #     return  self.subject

    # author 컬럼은 User 테이블의 외래키로 적용시킴
    # on_delete=models.CASCADE : 계정이 삭제되면 계정과 연결된
    #                            Question 테이블 데이터를 모두 삭제

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE )
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE )


