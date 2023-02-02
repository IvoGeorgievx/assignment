from django import forms
from django.contrib.auth import get_user_model

from assignment.web.models import Employees

UserModel = get_user_model()


class SignInForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


class EmployeeDeleteForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ()
