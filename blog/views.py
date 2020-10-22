from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Post

class PostList(generic.ListView): #the built in listview.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

@login_required
def add_blog(request):
    return render(request, 'blog/add_blog.html')