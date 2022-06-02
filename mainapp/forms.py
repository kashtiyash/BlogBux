from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Post
        fields = ('title', 'content')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class CommentsForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': "Add Comment here ...", 'rows': 4}))

    class Meta:
        model = Comments
        fields = ('content',)

