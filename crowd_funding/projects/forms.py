from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Projects , Images, Donation



class DateInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'details', 'category','user',
                  'total_target',  'start_time', 'end_time']
        widgets = {
            'start_time': DateInput(),
            'end_time': DateInput(),
            'user': forms.HiddenInput()
        }


class PictureForm(ModelForm):

    class Meta:
        model = Images
        fields = ['path']



class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'user' , 'project' ]
        widgets = {'project': forms.HiddenInput() , 'user': forms.HiddenInput()}






