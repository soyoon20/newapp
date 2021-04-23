from django.shortcuts import render, get_object_or_404, redirect
#--------------------------[edit]---------------------------------------------#
#from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Answer,Comment
from .forms import QuestionForm, AnswerForm,CommentForm
from django.contrib.auth.decorators import login_required
#----------------------------------------------------------------------------#
# 21/04/15 조준모 페이징처리 추가.
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def index(request):

    # get('page', '1') : 페이지의 파라미터가 없는 URL을 위해서
    # 기본값을 지정해 줬음
    page = request.GET.get('page', '1')
    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    # Paginator 클래스는 question_list를 페이징 객체(인스턴스)로 변환
    # 변환한 내용을 pagenator 객체(인스턴스)에 저장
    # Paginator 클래스를 호출하면서 두번째 인수에 페이지당 보여줄
    # 게시물 개수를 기재
    pagenator = Paginator(question_list, 5)
    # Paginator 클래스를 이용한 객체에 쓸수 있는 속성
    # .count : 게시물의 개수(전체)
    # .per_page : 페이지당 보여줄 게시물 개수
    # .page_range : 페이지의 범위
    # .number : 현재 페이지 번호
    # .previous_page_number : 이전 페이지 번호
    # .next_page_number : 다음 페이지 번호
    # .start_index : 현재 페이지 시작 인덱스
    # .end_index : 현재 페이지 끝 인덱스
    # .has_previous : 이전 페이지 유무(이전페이지가 있는지 없는지?)
    # .has_next : 다음 페이지 유무(다음페이지가 있는지 없는지?)
    page1 = pagenator.get_page(page)

    context = {'question_list1' : page1}

    return render(request, 'newapp/question_list.html', context)



#--------------------------[edit 21/04/13]---------------------------------------------#
def detail(request, question_id):

    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question1': question}
    return render(request, 'newapp/question_detail.html', context)

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


# 21/04/14 조준모 질문등록 함수 생성
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

# 질문에 댓글달기
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
# 복사해서 붙여넣기
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



