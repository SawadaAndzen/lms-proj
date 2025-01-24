from django import forms
from .models import JoinRequest


class RequestForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = ['user', 'course']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['course'].widget.attrs.update({'class': 'form-control'})