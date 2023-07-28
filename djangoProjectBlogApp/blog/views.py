from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

posts=[
    {
        'author':"Sudarshan",
        'title':"blog Post 1",
        'content':'This is the content by Sudarshan in blog Post 1',
        'date':'Aug 27th 2020'
    },
    {
        'author':"Jagruth",
        'title':"blog Post 2",
        'content':'This is the content by author in blog Post 2',
        'date':'Aug 27th 2020'
    }
]

def homeBlog(request):
    # return HttpResponse("<h1>Blog Home</h1>")
    return render(request,'blog/home.html',{"title":"Blog - Home "})

def aboutBlog(request):
    # return HttpResponse("<h1>Blog About</h1>")
    return render(request,'blog/about.html',{"title":"Blog - About"})

def postedPosts(request):
    context={
        "title":"Blog - Posts",
        "posts": Post.objects.all(),
    }
    return render(request,'blog/postedPosts.html',context)

def thankyou(request):
    return render(request, 'blog/thankyou.html',{"title":"THANK YOU -blog"})

class PostListView(ListView):
    model=Post
    template_name="blog/PostedPosts.html"
    context_object_name="posts"
    ordering=["-date"]

class PostDetailView(DetailView):
    model=Post
    # <app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['author','title','content']

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['author','title','content']

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/"
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
