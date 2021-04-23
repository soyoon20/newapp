# 2021년 4월 14일 장고 폼 작성

from .models import Question, Answer
from django import forms

from .models import  Question, Answer, Comment
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject' : '글 제목',
            'content' : '내용',
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields =['content2']
        labels = {
            'content2': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']
        labels = {
            'content': '댓글내용',
        }




