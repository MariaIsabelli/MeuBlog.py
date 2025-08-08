from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def novo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/novo_post.html', {'form': form})

def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('lista_posts')
    return render(request, 'blog/novo_post.html', {'form': form})

def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('lista_posts')


# Create your views here.
