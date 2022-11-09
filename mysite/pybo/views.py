from django.core.paginator import Paginator
from .forms import QuestionForm, AnswerForm
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Question
from django.utils import timezone


def question_create(request):
    """  pybo 질문 등록  """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm() # Get인 경우 호출함.
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


def index(request):
    """  pybo 목록 출력  """
    # 입력 인자
    page=request.GET.get('page', '1')  # 페이지

    # 조회
    question_list=Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 페이지장 10개씩 보여 주기
    page_obj = paginator.get_page(page)

    context={'question_list':page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """  pybo 내용 출력  """
    question=get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    """  pybo 답변 등록  """
    question = get_object_or_404(Question, pk=question_id) 
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit-False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question' : question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)