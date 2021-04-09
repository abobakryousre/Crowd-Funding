from .models import Comments, ReportedComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('message',)


class ReportCommentForm(forms.ModelForm):
    class Meta:
        model = ReportedComment
        fields = ('report_message',)
        widgets = {
            'report_message': forms.Textarea(attrs={
                'id': 'report-message',
                'required': True,
                'placeholder': 'Report message...'
            }),
        }
