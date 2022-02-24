from authapp.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''
