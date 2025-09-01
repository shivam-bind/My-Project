from django import forms

from .models import Post, BlogSubSection
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'image', 'content')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
                'rows': 5,
                'placeholder': 'Write your content...'
            }),
        }

class BlogSubSectionForm(forms.ModelForm):
    class Meta:
        model = BlogSubSection
        fields = ['sub_title', 'sub_content']

        widgets = {
            'sub_title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter sub_title'
            }),
            'sub_content': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
                'rows': 5,
                'placeholder': 'Write your sub_content...'
            }),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Enter your username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Enter your password"
        })
    )





class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = (
                'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none '
                'focus:ring-2 focus:ring-blue-400 focus:border-transparent'
            )


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = (
                'w-full px-3 py-2 border border-gray-300 rounded-lg '
                'focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent'
            )
