from django import forms
from .models import Comment, TaskAnswer


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "media"]
        labels = {'content': '', 'media': ''}
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'border:none; resize:none',
                'rows': 1,
                'cols': 50,
                'placeholder': 'Type here...',
            }),
            'media': forms.FileInput(attrs={
                'class': 'form-control d-none',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        
        
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