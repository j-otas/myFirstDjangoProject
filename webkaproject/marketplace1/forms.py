from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'cost', 'image', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'input_field'
        self.fields['title'].widget.attrs['placeholder'] = 'Название'
        self.fields['title'].label = ''

        self.fields['description'].widget.attrs['class'] = 'opisanie'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'
        self.fields['description'].label = ''

        self.fields['cost'].widget.attrs['class'] = 'input_field'
        self.fields['cost'].widget.attrs['placeholder'] = 'Цена'
        self.fields['cost'].label = ''


        # self.fields['username'].label = ''

        # self.fields['password'].widget.attrs['class'] = 'password_input'
        # self.fields['password'].label = ''

