from django.contrib.auth.models import User
from django.forms import ModelForm,forms
from .models import *

class register_form(ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

class update_profile(ModelForm):
    class Meta:
        model = emplyee_details
        fields = '__all__'

class leave_form(ModelForm):
    class Meta:
        model = leave_request
        fields = ['duration_from','duration_to','leave_msg']


