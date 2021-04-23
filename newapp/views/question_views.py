from django.shortcuts import render, get_object_or_404, redirect
#--------------------------[edit]---------------------------------------------#
#from django.http import HttpResponse
from django.utils import timezone
from newapp.models import Question
from newapp.forms import QuestionForm
from django.contrib.auth.decorators import login_required
#----------------------------------------------------------------------------#
# 21/04/15 조준모 페이징처리 추가.
from django.contrib import messages
# ----------------------------------------------------------------------------#
# 21/04/15 조준모 페이징처리 추가.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# --------------------------[edit]---------------------------------------------#
# from django.http import HttpResponse
from django.utils import timezone

from newapp.forms import QuestionForm
from newapp.models import Question

# module 임포트 한꺼번에 옮기기
# 컨트롤 + 알트 +알파벳 O

@login_required(login_url='common:login')

def question_create(request):

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'newapp/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('newapp:detail', question_id=question_id)

    if request.method == "POST":
        # instance 폼에서 받아온 내용의 내부구조를 정의할때 사용
        # 기존의 데이터를 받아와서 내용을 수정하기 위해 선언.
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('newapp:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'newapp/question_form.html', {'form': form})

@login_required(login_url='common:login')
def question_delete(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('newapp:detail', question_id=question_id)
    question.delete()
    return redirect('newapp:index')
