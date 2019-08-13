from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo

def index(request):
    mytodo = Todo.objects.order_by('id')

    form = TodoForm()
    context = {'mytodo': mytodo, 'form': form}

    return render(request, 'todo/index.html', context)
