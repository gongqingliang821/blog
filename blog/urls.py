from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^blog/$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentPostView.as_view(), name='comment'),
    url(r'^article/comment/$', views.CommentPostView.as_view(), name='comment1')
    ]
