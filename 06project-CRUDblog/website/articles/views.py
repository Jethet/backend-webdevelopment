from django.views.generic import ListView, DetailView
from . models import Article
from django.views.generic.edit import CreateView


class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'post'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'
