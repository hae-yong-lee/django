from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('<h1>랜덤 자료</h1>'+str(random.random()))

def create(request):
    return HttpResponse('안녕하세요. Create 페이지 입니다.')

def read(request, id):
    return HttpResponse('안녕하세요. Read 페이지 입니다.'+id)