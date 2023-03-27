from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        
        # Article.objects.create(
        #     title=title,
        #     content=content
        # )
        
        # article = Article(title=title, content=content)
        # article.save()

    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    # context = {'article': article}
    # return render(request, 'articles/detail.html', context)
    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article': article
#     }
    
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # if request.user == article.user:
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
        
        
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)