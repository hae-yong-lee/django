
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Question  # 75페이지에서 추가 내용
from django.utils import timezone

"""
from django.shortcuts import render
from .models import Question  # 75페이지에서 추가 내용


def index(request):

    question_list=Question.objects.order_by('-create_date')
    context={'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

"""



topics = [
    {'id':1, 'title':'대학소개', 'body':'대학소개입니다.'},
    {'id':2, 'title':'학과안내', 'body':'학과안내입니다.'},
    {'id':3, 'title':'학사정보', 'body':'학사정보입니다.'},
] 

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
       ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">대표 홈페이지</a></h>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/pybo/">학과안내</a></li>
        </ul>
    </body>
    </html>
    '''

# Create your views here.
def index(request):

#  ==============여기서부터 75 페이지 내용 입력   
#            
#    pybo 목록출력
#
    question_list=Question.objects.order_by('-create_date')
    context={'question_list':question_list}
#  ============== 여기까지 입력함. 

    article = '''
    <h2>환영합니다.</h2>
    안녕, 구미대학교
    '''
 #   return HttpResponse(HTMLTemplate(article))
    return render(request, 'pybo/question_list.html', context)

@csrf_exempt
def pybo(request):
    article = '''
        <form action="/pybo/" method="post">
            <p><input type="text" name="제목입력" placeholder="title"></p>
            <p><textarea name="body" placeholder="본문입력"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))


def read(request, id):  
    global topics
    article = ''
    for topic in topics:
       if topic['id'] == int(id):
         article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question=get_object_or_404(Question, pk=question_id)
#    question=Question.objects.get(id=question_id)
    context={'question':question}
    return render(request, 'pybo/question_detail.html', context)

"""
def answer_create(request, question_id):
    
    답변등록
    
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)
"""

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)