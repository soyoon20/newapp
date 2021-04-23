from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
#--------------------------[edit]---------------------------------------------#
#from django.http import HttpResponse

from ..models import Question, Answer,Comment

#----------------------------------------------------------------------------#
# 21/04/15 조준모 페이징처리 추가.

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




