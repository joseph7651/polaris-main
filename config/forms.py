from django import forms
from django.contrib.auth.models import User
from insights.models import UserProfile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'color: black;',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'color: black;',
        })
    )

# touched on 2025-05-27T15:28:51.111952Z
# touched on 2025-05-27T15:28:53.860787Z
# touched on 2025-05-27T15:28:59.284261Z
# touched on 2025-08-14T21:16:34.770958Z
# touched on 2025-08-14T21:16:47.630173Z
# touched on 2025-08-14T21:16:51.812172Z
# touched on 2025-08-14T21:17:11.394439Z
# touched on 2025-08-14T21:17:24.371536Z
# touched on 2025-08-14T21:17:30.625716Z
# touched on 2025-08-14T21:17:43.312534Z
# touched on 2025-08-14T21:18:06.134023Z
# touched on 2025-08-14T21:18:16.428692Z
# touched on 2025-08-14T21:18:22.659814Z
# touched on 2025-08-14T21:18:32.927937Z