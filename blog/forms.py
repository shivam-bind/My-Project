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
                'class': 'w-full p-3 border rounded-xl shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-300 ease-in-out hover:shadow-md',
                'placeholder': '✨ Enter a catchy title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 border rounded-xl shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-300 ease-in-out hover:shadow-md',
                'rows': 5,
                'placeholder': '✍️ Write your amazing content here...'
            }),
        }


class BlogSubSectionForm(forms.ModelForm):
    class Meta:
        model = BlogSubSection
        fields = ['sub_title', 'sub_content']

        widgets = {
            'sub_title': forms.TextInput(attrs={
                'class': 'w-full p-3 border rounded-xl shadow-sm focus:ring-2 focus:ring-green-500 focus:border-green-500 transition duration-300 ease-in-out hover:shadow-md',
                'placeholder': '📌 Enter sub title'
            }),
            'sub_content': forms.Textarea(attrs={
                'class': 'w-full p-3 border rounded-xl shadow-sm focus:ring-2 focus:ring-green-500 focus:border-green-500 transition duration-300 ease-in-out hover:shadow-md',
                'rows': 5,
                'placeholder': '📝 Write sub content here...'
            }),
        }


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full border rounded-xl px-4 py-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition duration-300 ease-in-out hover:shadow-md",
            "placeholder": "👤 Enter your username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full border rounded-xl px-4 py-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition duration-300 ease-in-out hover:shadow-md",
            "placeholder": "🔒 Enter your password"
        })
    )









# from django import forms

# from .models import Post, BlogSubSection
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import User

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = ('title', 'image', 'content')

#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
#                 'placeholder': 'Enter title'
#             }),
#             'content': forms.Textarea(attrs={
#                 'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
#                 'rows': 5,
#                 'placeholder': 'Write your content...'
#             }),
#         }

# class BlogSubSectionForm(forms.ModelForm):
#     class Meta:
#         model = BlogSubSection
#         fields = ['sub_title', 'sub_content']

#         widgets = {
#             'sub_title': forms.TextInput(attrs={
#                 'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
#                 'placeholder': 'Enter sub_title'
#             }),
#             'sub_content': forms.Textarea(attrs={
#                 'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-400',
#                 'rows': 5,
#                 'placeholder': 'Write your sub_content...'
#             }),
#         }

# class CustomLoginForm(AuthenticationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={
#             "class": "w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
#             "placeholder": "Enter your username"
#         })
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             "class": "w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
#             "placeholder": "Enter your password"
#         })
#     )

