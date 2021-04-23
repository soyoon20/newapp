
from django.shortcuts import render, get_object_or_404, redirect
#--------------------------[edit]---------------------------------------------#
#from django.http import HttpResponse
from django.utils import timezone
from newapp.models import Question, Answer
from newapp.forms import AnswerForm
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

from newapp.forms import AnswerForm
from newapp.models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date2 = timezone.now()
            answer.question = question
            answer.save()
            return redirect('newapp:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question1': question, 'form': form}
    return render(request, 'newapp/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, question_id):
    question = get_object_or_404(Answer, pk=answer_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('newapp:detail', question_id=answer.question.id)

    if request.method == "POST":
        # instance 폼에서 받아온 내용의 내부구조를 정의할때 사용
        # 기존의 데이터를 받아와서 내용을 수정하기 위해 선언.
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('newapp:detail', question_id=answer.question_id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'newapp/answer_form.html', {'answer':answer, 'form': form})

@login_required(login_url='common:login')
def answer_delete(request, answer_id):

    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('newapp:detail', question_id=answer.question_id)
    else:

         answer.delete()
    return redirect('newapp:detail', question_id=answer.question_id)

