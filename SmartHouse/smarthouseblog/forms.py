from django import forms
from django.forms import Textarea

from .models import Blog, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "title",
            "text",
            "category",
            "status",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            "comment",
            "raiting",
        )
        widgets = {
            'comment': Textarea(attrs={'rows': 4, 'cols': 40}),
        }