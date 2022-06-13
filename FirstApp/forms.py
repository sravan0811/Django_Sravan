from django import forms
from django.core import  validators
from .models import UserFormMy
from django.contrib.auth.models import User
from .models import UserProfileInfo

def check_for_data(value):
    if value[0].lower() !='a':
        raise forms.ValidationError("Name need to start with a")

class FormName(forms.Form):
    name = forms.CharField( validators=[validators.MaxLengthValidator(0)])
    email = forms.EmailField(validators=[check_for_data])
    verify_email = forms.EmailField(label="Enter the Email Once Again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Emails Must Match")


class NewUser(forms.ModelForm):
    class Meta():
        model = UserFormMy
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
