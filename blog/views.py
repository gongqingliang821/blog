#coding=UTF-8
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article
from blog.models import Category
from django.views.generic.edit import FormView
from blog.forms import BlogCommentForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect,get_object_or_404
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"
    model = Article

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        context=super(IndexView, self).get_context_data(**kwargs)
        return context

class CategoryView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"
    def get_queryset(self):
        article_list =  Article.objects.filter(category=self.kwargs['cate_id'], status='p')

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        context = super(CategoryView, self).get_context_data(**kwargs)
        return context



class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = self.object.blogcomment_set.all()
        kwargs['len'] = len(kwargs['comment_list'])
        kwargs['form'] = BlogCommentForm()
        context=super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

class CommentPostView(FormView):
    form_class = BlogCommentForm
    template_name = 'blog/detail.html'
    #success_url = reverse_lazy('blog:index',kwargs={'article_id': self.pk})
    def form_valid(self, form):
        self.success_url = reverse_lazy('blog:detail',kwargs={'article_id': self.kwargs['article_id']})
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        comment = form.save(commit=False)
        comment.article = target_article
        comment.save()
        return HttpResponseRedirect(self.success_url)


    def form_invalid(self, form):
        print "hello"
        print self.request





