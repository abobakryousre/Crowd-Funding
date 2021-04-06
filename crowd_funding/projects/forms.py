from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Projects, Images, Donation
from .models.reported_project import ReportedProject


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'details', 'category', 'user',
                  'total_target', 'start_time', 'end_time']
        widgets = {
            'start_time': DateInput(),
            'end_time': DateInput(),
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'blue-field-area'


# class PictureForm(ModelForm):
#     class Meta:
#         model = Images
#         fields = ['path']


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'user', 'project']
        widgets = {'project': forms.HiddenInput(), 'user': forms.HiddenInput()}


class ReportProjectForm(forms.ModelForm):
    class Meta:
        model = ReportedProject
        fields = ('report_message',)
        widgets = {
            'report_message': forms.Textarea(attrs={
                'id': 'report-project-message',
                'required': True,
                'placeholder': 'Report message...'
            }),
        }
