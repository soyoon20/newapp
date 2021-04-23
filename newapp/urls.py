"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import answer_views, base_views, comment_views, question_views

# url에 별칭을 부여하는것은
# 실제 주소명은 /newapp/은 index라는 url 별징으로 변경
# /newapp/question_id  detail로 변경
# 앱을 추가할때 다른앱에서 url 별칭이 중복되면 안된다.
# url 설정할때 네임스페이스를 이용해서 독립된 이름 공간을 생성할것.
# 네임스페이스: 각각의 앱이 관리하는 공간

# 21/04/13 네임스페이스 추가---------------------------
# 네임스페이스 변수를 만든다면 저장되는 문자열값은 앱 이름과 동일하게 하는것이 편하다
# 게시글 답변작성 페이지 추가
app_name = 'newapp'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),

    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
]