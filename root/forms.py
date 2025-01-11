from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
        

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