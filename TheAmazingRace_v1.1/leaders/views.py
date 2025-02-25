from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@login_required add when authenticication is required
def login(request):
    return render(request, '../templates/login.html')

#@login_required add when authenticication is required
def leadersHome(request):
    return render(request, '../templates/leaderHome.html')

# Create your views here.
def makeQuestions(request):
    return render(request, '../templates/makeQuestions.html')