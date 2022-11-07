from .forms import QuestionForm
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
    question_list=Question.objects.order_by('-create_date')
    context={'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """  pybo 내용 출력  """
    question=get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    """  pybo 답변 등록  """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)