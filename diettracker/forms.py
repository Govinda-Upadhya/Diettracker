from django import forms
    
class SignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    username=forms.CharField(max_length=100,label="Username")
    first_name=forms.CharField(max_length=100,label="First Name")
    last_name=forms.CharField(max_length=100,label="Last Name")
    email=forms.EmailField(label="Email")
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
    reenter=forms.CharField(widget=forms.PasswordInput,label="Confirm")
class SignInForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'un '
        self.fields['password'].widget.attrs['class'] = 'pass '
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    username=forms.CharField(max_length=100,label="Username")
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
   