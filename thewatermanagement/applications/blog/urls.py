from django.urls import include, path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path(
        '',
        views.BlogListView.as_view(),
        name='list_blog'
    ),
    path(
        'detail_post/<pk>/',
        views.PostDetailView.as_view(),
        name='detail_post'
    )
]