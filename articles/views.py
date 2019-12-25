# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import (ListView, UpdateView, DeleteView, DetailView,CreateView)
from .models import Article
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import jsonarticle
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_add.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = jsonarticle
    queryset = Article.objects.all()


class ArticleCreateREST(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = jsonarticle


class a(APIView):
    def get(self, request, forma=None):
        users = [article.id for article in Article.objects.all()]
        return Response(users)
