from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField( label='Имя пользователя', widget= forms.TextInput(attrs={'class':'register'}))
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class':'register'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class':'register'})),
    password2 = forms.CharField(label="Подтверждение пароля",widget=forms.PasswordInput(attrs={'class':'register'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'register'}),
        #     'email': forms.EmailInput(attrs={'class':'register'}),
        #     'password1': forms.PasswordInput(attrs={'class':'register'}, ),
        #     'password2': forms.PasswordInput(attrs={'class':'register'}),
        # }


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)