from django import forms

from .models import Post


class ProductForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
