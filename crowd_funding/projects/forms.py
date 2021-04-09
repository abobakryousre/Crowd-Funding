import datetime

from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Projects, Images, Donation
from .models.reported_project import Report


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


    def clean(self):

        super(ProjectForm, self).clean()
        total_target = self.cleaned_data['total_target']
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']

        if float(total_target) <= 0:
            self._errors['total_target'] = self.error_class([
                'Total target cannot start with value less than zero'])
            # raise forms.ValidationError("Total target cannot start with value less than zero")

        if start_time < datetime.date.today():
            self._errors['start_time'] = self.error_class([
                'start date can not be before the current date'])
        if end_time < start_time:
            self._errors['end_time'] = self.error_class([
                'end date can not be before the start date'])
        return self.cleaned_data



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
        model = Report
        fields = ('report_message',)
        widgets = {
            'report_message': forms.Textarea(attrs={
                'id': 'report-project-message',
                'required': True,
                'placeholder': 'Report message...'
            }),
        }
