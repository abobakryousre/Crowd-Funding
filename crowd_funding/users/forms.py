from django.contrib.auth import authenticate

from users.models import User
from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm, models

from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth.models import User


class createuserform(UserCreationForm):
    phone_number = forms.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex=r'(01)[0-9]{9}$',
                message="Phone number must be entered in the egyption format"
            ),
        ],
    )

    # profile_picutre = forms.ImageField( )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2", "phone_number", "profile_picutre")

class loginformauth(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.passwordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('invalied login')

#
#
# class Usermodelform(ModelForm):
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name","username", "email", "password", "mobile_phone","country","birth_date")
