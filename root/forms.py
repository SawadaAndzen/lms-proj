from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Message, Role


#AUTH
class CustomSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username", "first_name",
            "last_name", "password1",
            "password2"
        ]
    
    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.update({"class": "form-control", 'placeholder': 'Letters, digits and @/./+/-/_ only.'})
        self.fields["first_name"].widget.attrs.update({"class": "form-control", 'placeholder': 'First name (Required.)', 'required': 'required'})
        self.fields["last_name"].widget.attrs.update({"class": "form-control", 'placeholder': 'Last name (We`re recommend not leaving it blank.)'})
        self.fields["password1"].widget.attrs.update({"class": "form-control", 'placeholder': 'Enter a strong password.'})
        self.fields["password2"].widget.attrs.update({"class": "form-control", 'placeholder': 'Confirm your password.'})
        
        self.fields["username"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        
        
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        
   
#USER CUSTOMIZATION
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New first name.'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New last name.'})
        
        self.fields.pop('password', None)
        
        
class CustomChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
        
    def __init__(self, *args, **kwargs):
        super(CustomChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old password.'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New password.'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm new password.'})
        
        self.fields['new_password1'].help_text = None
        
        
#PROFILE
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pfp', 'desc']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['pfp'].widget.attrs.update({'class': 'form-control'})
        self.fields['desc'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['desc'].required = False
        
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
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
        super(MessageForm, self).__init__(*args, **kwargs)
        
        
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ["user", "role"]
        
    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({'class': 'form-control', 'placeholder': ''})
        self.fields['role'].widget.attrs.update({'class': 'form-control', 'placeholder': ''})