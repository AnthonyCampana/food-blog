from django import forms


class registrationForm(forms.Form):

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    userName = forms.CharField(label="userName", max_length=32)
    password = forms.CharField(label="password", max_length=24)
    retypePassword = forms.CharField(label="retype-password", max_length=24)
    email = forms.EmailField()

class LoginForm(forms.Form):

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    userName = forms.CharField(label="UserName", max_length=32) 
    password = forms.CharField(label="password", max_length=24)