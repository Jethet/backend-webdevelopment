from django.shortcuts import render

def index(request):
    return render(request, 'videorequest/index.html')


def vrform(request):
    return render(request, 'videorequest/vrform.html')
