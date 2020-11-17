from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from .forms import JobSearchForm
from django.urls import reverse
from utils.search import get_job_list
# Create your views here.


# def home(request):
#     print("Hello")
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


def home(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, "blog/prehome.html")


def job_search(request):
    print("hello")
    if request.method == "POST":
        form = JobSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            job_title = data['job_title']
            location = data['location']
            print(job_title, location)
            return redirect(f'/job_results/{job_title}/{location}')
    else:
        form = JobSearchForm()
    return render(request, 'blog/job_page.html', {'form': form})


def job_result(request, job_title, location):
    results = get_job_list(job_title, location)
    print(results)
    return render(request, 'blog/job_results.html', {'results': results})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

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
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
