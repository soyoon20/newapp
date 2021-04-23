#0419회원가입 폼 작성
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# UserCreationForm을 이용해서
# 회원가입의 기본 속성을 받아올수 있다
# 받아오는 기본 속성은 username,password1,password2를 받아올수 있다.
# email등 다른 속성들응 추가해서 회원가입시 입력하게 만들수 있다
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields =("username", "email")

        # Meta클래스 UserForm의 내부 클래스
