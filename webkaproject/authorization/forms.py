from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from marketplace1.models import UserDetails


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['username'].widget.attrs['class'] = 'username_input'
        self.fields['username'].label = ''
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password'].widget.attrs['class'] = 'password_input'
        self.fields['password'].label = ''



class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets={
            'password': forms.PasswordInput()
        }
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин'
            self.fields['username'].widget.attrs['class'] = 'username_input'
            self.fields['username'].label = ''
            self.fields['username'].help_text = ''
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль'
            self.fields['password'].widget.attrs['class'] = 'password_input'
            self.fields['password'].label = ''


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('country', 'cellphone')

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['cellphone'].widget.attrs['placeholder'] = 'Номер телефона'
            self.fields['cellphone'].widget.attrs['class'] = 'input_field'
            self.fields['cellphone'].label = ''
            self.fields['cellphone'].help_text = ''
            self.fields['country'].widget.attrs['placeholder'] = 'Город'
            self.fields['country'].widget.attrs['class'] = 'input_field'
            self.fields['country'].label = ''


    def save(self, commit=True):
        user = super().save(commit=False)
        # user.set_password(self.cleaned_data["password"])
        # if commit:
        #     user.save()
        return user