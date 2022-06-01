from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class signupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __int__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)

        for filename in ['username', 'email', 'password1', 'password2']:
            self.fields[filename].help_text = None
