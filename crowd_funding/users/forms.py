from django import forms
from users.models import User

class UserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'country', 'profile_picutre', 'mobile_phone', 'birth_date']

    widgets = {
        "first_name": forms.TextInput(attrs={ 'class': 'form-control' }),
        "last_name": forms.TextInput(attrs={ 'class': 'form-control' }),
        "country": forms.Select(attrs={ 'class': 'form-control' }),
        "profile_picutre": forms.FileInput(attrs={ 'class': 'form-control' }),
        "mobile_phone": forms.NumberInput(attrs={ 'class': 'form-control' }),
        "birth_date": forms.DateInput(attrs={ 'class': 'form-control' }),

    }
