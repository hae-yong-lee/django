from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'},
]
# Create your views here.
def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcom</h2>
        Hello, Django
    </body>
    </html>
    ''')

def create(request):
    return HttpResponse('안녕하세요. Create 페이지 입니다.')

def read(request, id):
    return HttpResponse('안녕하세요. Read 페이지 입니다.'+id)