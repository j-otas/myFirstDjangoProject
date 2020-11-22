from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User

        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'E-Mail'
        self.fields['username'].widget.attrs['class'] = 'username_input'
        self.fields['username'].label = ''
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password'].widget.attrs['class'] = 'password_input'
        self.fields['password'].label = ''
