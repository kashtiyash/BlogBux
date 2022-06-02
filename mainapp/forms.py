from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Post
        fields = ('title', 'content')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
