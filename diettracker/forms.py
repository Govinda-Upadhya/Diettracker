from django import forms
    
class SignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    username=forms.CharField(max_length=100,label="username")
    first_name=forms.CharField(max_length=100,label="first_name")
    last_name=forms.CharField(max_length=100,label="last_name")
    email=forms.EmailField(label="email")
    password=forms.CharField(widget=forms.PasswordInput,label="password")
    reenter=forms.CharField(widget=forms.PasswordInput,label="confirm")
class SignInForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
   