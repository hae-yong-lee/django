from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question  # 75페이지에서 추가 내용


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
    
    """               
    pybo 목록출력
    """
    question_list=Question.objects.order_by('-create_date')
    context={'question_list':question_list}

    article = '''
    <h2>환영합니다.</h2>
    안녕, 구미대학교
    '''
    return HttpResponse(HTMLTemplate(article))

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