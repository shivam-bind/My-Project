from django import forms

from .models import Post, BlogSubSection

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'image', 'content')



class BlogSubSectionForm(forms.ModelForm):
    class Meta:
        model = BlogSubSection
        fields = ['sub_title', 'sub_content']