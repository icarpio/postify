from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required  # Asegúrate de que el usuario esté autenticado
def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Asegúrate de manejar archivos
        if form.is_valid():
            post = form.save(commit=False)  # No guardar aún
            post.user = request.user  # Asigna el usuario conectado
            post.save()  # Ahora guarda el post
            return redirect('posts')  # Redirige a donde desees después de crear el post
    else:
        form = PostForm()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'form': form, 'posts': posts})

@login_required
def user_posts_view(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at') # Filtra los posts del usuario actual
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def all_posts_view(request):
    
    posts = Post.objects.all().order_by('-created_at')  # Obtiene todos los posts
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Obtiene el post específico por su ID
    return render(request, 'posts/post_detail.html', {'post': post})

