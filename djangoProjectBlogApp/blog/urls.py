from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns=[
    path('',views.homeBlog,name="blog-home"),
    path('about/',views.aboutBlog,name="blog-about"),
    path('posts/',PostListView.as_view(),name="blog-posts"),
    path('posts/<int:pk>/',PostDetailView.as_view(),name="posts-detail"),
    path('posts/new/',PostCreateView.as_view(),name="posts-create"),
    path('posts/<int:pk>/update',PostUpdateView.as_view(),name="posts-update"),
    path('posts/<int:pk>/delete',PostDeleteView.as_view(),name="posts-delete"),
    
    # path('thankyou/',views.thankyou,name="blog-thankYou")
]