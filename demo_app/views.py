from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from demo_app.models import Article, Author, Theme, Comics
from demo_app.forms import ArticleForm, AuthorForm
from demo_app.models import Article
from datetime import datetime
from django import views
from demo_app.serializer import ArticleSerializer
from rest_framework.parsers import JSONParser
from django.views.generic import CreateView, ListView, DetailView, UpdateView

# Create your views here.

def dashboard(request):
    data = ['Hike to Bandipur', "hike to namobuddha"]
    return render(request, 'home.html', {'data': data, 'show_post': False})

def list_art(request):
    article_list = Article.objects.all()
    return render(request,"list_articles.html", context = {'data': article_list})

# def add_article(request):
#     if request.method == 'GET':
#         return render(request, 'add_article.html')
#     elif request.method == 'POST':
#         data = request.POST
#         print(data)
#         return redirect('list_articles')

def add_article(request):
    if request.method == 'GET':
        return render(request, 'add_article.html', {'form': ArticleForm(), 'theme': Theme.objects.all()})
    elif request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # article = Article(user = request.POST['user'], conent = request.POST['conent'], no_likes = request.POST['no_likes'],
            #                   date_posted = datetime.now().date())
            # article.save()
            article = form.save(commit=False)
            article.date_posted = datetime.now().date()
            article.save()
            for id in request.POST.getlist('theme'):
                theme =Theme.objects.get(id=id)
                theme.article.add(article)

            print(request.POST)

            return redirect('list_articles')
        else:
            return render(request, 'add_article.html', {'form': form})

def edit_article(request, id):
    art = Article.objects.get(id=id)

    if request.method == 'GET':
        form = ArticleForm(instance = art)

        return render(request, 'edit_article.html', {'form': form, 'id': id})
    elif request.method == 'POST':
        form = ArticleForm(request.POST, instance= art)
        if form.is_valid():
            art = form.save()
            return redirect('list_articles')
        else:
            return render(request, 'add_article.html', {'form': form})

def delete_article(request, id):

    if request.method == 'GET':
        art = Article.objects.get(id=id)
        return render(request, 'delete_article.html', {"data": art})
    elif request.method == 'POST':
        art = Article.objects.get(id=id)
        art.delete()
        return redirect('list_articles')

def list_author(request):
    author_list = Author.objects.all()
    return render(request, "list_author.html", context={'data': author_list})


def add_author(request):
    if request.method == 'GET':
        return render(request, 'add_author.html', {'form': AuthorForm()})
    elif request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit = False)
            author.date_posted = datetime.now().date()
            author.save()

            return redirect('list_article')
        else:
            return render(request, 'add_author.html', {'form': form})

def edit_author(request, id):
    aut = Author.objects.get(id=id)

    if request.method == 'GET':
        form = AuthorForm(instance = aut)

        return render(request, 'edit_author.html', {'form': form, 'id': id})
    elif request.method == 'POST':
        form = AuthorForm(request.POST, instance= aut)
        if form.is_valid():
            aut = form.save()
            return redirect('list_author')
        else:
            return render(request, 'add_author.html', {'form': form})

def delete_author(request, id):
    if request.method == 'GET':
        art = Author.objects.get(id=id)
        return render(request, 'delete_author.html', {"data": art})
    elif request.method == 'POST':
        art = Author.objects.get(id=id)
        art.delete()
        return redirect('list_author')

def detail_author(request, id):
    author = Author.objects.get(id=id)
    return render(request, "detail_author.html", context={'data': author})

class ArticleAPIView(views.View):
    def get(self, request, id):
        art = Article.objects.get(id=id)
        ser = ArticleSerializer(art)
        return JsonResponse(ser.data, status=200)


    # delete method
    def delete(self, request, id):
        art = Article.objects.get(id=id)
        art.delete()
        return HttpResponse(status=200)

    def put(self, request, id):
        data = JSONParser().parse(request)
        art = Article.objects.get(id =id)
        ser = ArticleSerializer(instance =art, data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        else:
            return JsonResponse(ser.errors, status=302)

class MultiArticleAPIView(views.View):
    def get(self, request):
        art_list = Article.objects.all()
        ser = ArticleSerializer(art_list, many=True)
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        data =JSONParser().parse(request)
        ser =ArticleSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
        else:
            JsonResponse(ser.errors, status=302)

class AddComics(CreateView):
    model = Comics
    template_name = 'add_comics.html'
    fields = '__all__'
    success_url = reverse_lazy('list_comics')
    # success_url = '/'

class ListComics(ListView):
    model = Comics
    template_name = 'list_comics.html'

class UpdateComics(UpdateView):
    model = Comics
    fields = '__all__'
    success_url = reverse_lazy('list_comics')
    template_name = 'update_comics.html'














