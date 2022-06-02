from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, PostUpdateForm

# Create your views here.


def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('Home')
    else:
        form = PostForm()

    contex = {
            'posts': posts,
            'form': form,
    }
    return render(request, 'mainapp/index.html', contex)


def contact(request):
    return render(request, 'mainapp/contact.html')


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,

    }
    return render(request, 'mainapp/post_details.html', context)


def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form =PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details', pk=post.id)
    else:
        form = PostUpdateForm()
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'mainapp/post_edit.html', context)


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('Home')
    context = {
        'post': post,
    }
    return render(request, 'mainapp/post_delete.html', context)