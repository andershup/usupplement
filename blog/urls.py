from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_blog/', views.add_blog , name='add_blog'),
]