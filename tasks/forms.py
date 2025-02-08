from django import forms
from .models import TaskAnswer
        
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = TaskAnswer
        fields = ["media"]
        labels = {'media': ''}
        widgets = {
            'media': forms.FileInput(attrs={
                'class': 'form-control d-none',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)