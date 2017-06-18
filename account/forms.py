from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,UserInfo
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username","email")
    def cleand_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("password not match")
        return cd["password2"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone","birth")

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school","company","profession","address","aboutme","photo")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)

