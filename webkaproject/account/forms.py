from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 60, help_text = "Рекуайред. Add a valid email add")
    cellphone = PhoneNumberField()
    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name", "username", "country", "cellphone", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'E-Mail'
        self.fields['email'].widget.attrs['class'] = 'input_field'
        self.fields['email'].label = ''
        self.fields['email'].help_text = ''

        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['first_name'].widget.attrs['class'] = 'input_field'
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = ''

        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['last_name'].widget.attrs['class'] = 'input_field'
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Никнейм'
        self.fields['username'].widget.attrs['class'] = 'input_field'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['country'].widget.attrs['placeholder'] = 'Город'
        self.fields['country'].widget.attrs['class'] = 'input_field'
        self.fields['country'].label = ''
        self.fields['country'].help_text = ''

        self.fields['cellphone'].widget.attrs['placeholder'] = 'Номер телефона'
        self.fields['cellphone'].widget.attrs['class'] = 'input_field'
        self.fields['cellphone'].label = ''
        self.fields['cellphone'].help_text = ''

        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].widget.attrs['class'] = 'input_field'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].widget.attrs['class'] = 'input_field'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''