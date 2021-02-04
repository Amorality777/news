from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import CommentForm, NewsForm
from .models import News, Comments
from django.views.generic import ListView, CreateView


class NewsView(ListView):
    model = News
    context_object_name = 'news_list'


class NewsDetailView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        if request.user.is_authenticated:
            comment_form = CommentForm(initial={'username': request.user.username})
            comment_form.fields['username'].widget = HiddenInput()
        else:
            comment_form = CommentForm()
        return render(request, 'app_news/news_detail.html',
                      context={'news': news, 'comment_form': comment_form})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                Comments.objects.create(**comment_form.cleaned_data, news=news, user=request.user)
            else:
                username = comment_form.cleaned_data['username'] + ' *anonymous*'
                comment = comment_form.cleaned_data['comment']
                Comments.objects.create(username=username, comment=comment, news=news)
            return HttpResponseRedirect(reverse('news_detail', kwargs={'news_id': news_id}))
        return render(request, 'app_news/news_detail.html', context={'news': news, 'comment_form': comment_form})


class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'content', 'status']


class NewsEditView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/newsedit_news.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news.save()
        return render(request, 'app_news/newsedit_news.html', context={'news_form': news_form, 'news_id': news_id})
