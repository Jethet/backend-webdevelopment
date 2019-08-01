from django.views.generic import ListView
from .models import Command

class HomePageView(ListView):
    model = Command
    template_name = 'home.html'
