from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'form': form, 'posts': posts})

