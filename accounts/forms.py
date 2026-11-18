
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = [
            'full_name',
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email
