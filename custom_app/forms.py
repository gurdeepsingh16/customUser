from custom_app.models import User
from django import forms

class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','mobile','email','password'] 

