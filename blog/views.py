from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'title': 'Blog Home page'}
    return render(request, 'blog/home.html', context)


# replacing the above def home(request) function based view with class based view.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    # default naming convention is <appname>/<modelname>_<viewtype>.html
    context_object_name = 'posts'  # default name is object.
    ordering = ['-date_posted']
    paginate_by = 6


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    # default naming convention is <appname>/<modelname>_<viewtype>.html
    context_object_name = 'posts'  # default name is object.
    paginate_by = 6

    # To filter the posts on the basis of users - override the get_queryset method
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
    # the parameters context_object_name and template_name are needed only if we are
    # not following the django convention.


# The mixins need to be to the left of the View inheritance.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    # the parameters context_object_name and template_name are needed only if we are
    # not following the django convention.

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # To add the author in the form as the current user - override the form_valid method.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')
