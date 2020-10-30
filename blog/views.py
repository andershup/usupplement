from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import Post
from .forms import BlogForm


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'your blog has been added!')
            return redirect(reverse('add_blog'))
        else:
            messages.error(request, 'Ups! Try that again')
    else:
        form = BlogForm()
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
