from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, code, commit=True, *args, **kwargs):
        user = super(UserCreationForm, self).save(commit=False, *args, **kwargs)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.profile.verification_code = code
            user.profile.is_verified = False
            user.save()
        return user
