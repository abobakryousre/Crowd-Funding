from django.forms import ModelForm
from users.models import User

class UserProfile(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'country', 'profile_picutre', 'mobile_phone', 'birth_date']

