from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup
import json
import requests
# Create your views here.

def index(request):
    return HttpResponse("success")

class QuestonAPI(viewsets.ModelViewSet):
    queryset= Question.objects.all()
    serializer_class=QuestionSerializer

def latest(request):    
    try:    
        res = requests.get("https://stackoverflow.com/questions")
        soup = BeautifulSoup(res.text,"html.parser")
        questions = soup.select(".question-summary")
        for que in questions:
            q=que.select_one('.question-hyperlink').getText()
            vote=que.select_one('.vote-count-post').getText()
            views=que.select_one('.views').getText()
            tags=[i.getText() for i in (que.select(".post-tag"))]

            question = Question()
            question.question=q
            question.vote=vote
            question.views=views
            question.tags=tags 

            question.save()
        return HttpResponse("Latest Data Fetched") 
    except e as Exception:
        return HttpResponse("Failed {e}")