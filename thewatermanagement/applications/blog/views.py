from django.shortcuts import render
from django.utils import timezone
from applications.blog.models import Post
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

# Create your views here.
class BlogListView(ListView):
    template_name = 'blog/blog.html'
    def get_queryset(self):
        object_list = Post.objects.all()
        return object_list

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail_post.html"