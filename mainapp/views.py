from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

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


