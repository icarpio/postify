from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
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
    posts = Post.objects.filter(user=request.user).order_by('-created_at') #Muestra los posts del propio usuario
    return render(request, 'posts/post_list.html', {'form': form, 'posts': posts})

@login_required
def user_posts_view(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at') # Filtra los posts del usuario actual
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def all_posts_view(request):
    posts = Post.objects.all().order_by('-created_at')  # Obtiene todos los posts
    return render(request, 'posts/all_post_list.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()  # Obtener comentarios asociados al post
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Asignar el usuario actual
            comment.post = post  # Asignar el post actual
            comment.save()
            return redirect('post_detail', post_id=post.id)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')  # Redirige a la lista de posts
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    # Verificar que el post realmente exista y que el usuario sea el propietario
    post = get_object_or_404(Post, id=post_id, user=request.user)
    
    # Verificar si la solicitud es un POST, entonces eliminamos el post
    if request.method == 'POST':
        post.delete()  # Eliminar el post
        return redirect('posts')  # Redirigir a la lista de posts
