from django import forms
from .models import Class


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'desc', 'course', 'teacher', 'students']
        
    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        
        self.fields["name"].widget.attrs.update({"class": "form-control", 'placeholder': 'Group name.'})
        self.fields["desc"].widget.attrs.update({"class": "form-control", 'placeholder': 'Description.'})
        self.fields["course"].widget.attrs.update({"class": "form-control", 'placeholder': 'Course.'})
        self.fields["teacher"].widget.attrs.update({"class": "form-control", 'placeholder': 'Group teacher.'})
        self.fields["students"].widget.attrs.update({"class": "form-control", 'placeholder': 'Group students.'})