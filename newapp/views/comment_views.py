
from django.shortcuts import render, get_object_or_404, redirect
#--------------------------[edit]---------------------------------------------#
#from django.http import HttpResponse
from django.utils import timezone
from newapp.models import Question, Answer,Comment
from newapp.forms import CommentForm
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

from newapp.forms import CommentForm
from newapp.models import Question, Answer, Comment


@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):

    answer= get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('newapp:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm()
    return render(request, 'newapp/comment_form.html', {'form': form})

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('newapp:detail', question_id=comment.answer.question_id)


    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('newapp:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'newapp/comment_form.html', {'form': form})

@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('newapp:detail', question_id=comment.answer.question.id)
    else:

         comment.delete()
    return redirect('newapp:detail', question_id=comment.answer.question.id)

@login_required(login_url='common:login')
def comment_create_question(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('newapp:detail', question_id=question_id)
    else:
        form = CommentForm()
    return render(request, 'newapp/comment_form.html', {'form': form})


@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('newapp:detail', question_id=comment.question_id)


    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('newapp:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'newapp/comment_form.html', {'form': form})

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('newapp:detail', question_id=comment.question_id)
    else:

         comment.delete()
    return redirect('newapp:detail', question_id=comment.question_id)