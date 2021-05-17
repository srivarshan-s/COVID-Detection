from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from covid.models import Doctor


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={'class': "input1"}), required=True)
    password1 = forms.CharField(
        max_length=25, widget=forms.PasswordInput(
            attrs={'class': "input1"}), required=True)
    password2 = forms.CharField(
        max_length=25, widget=forms.PasswordInput(
            attrs={'class': "input1"}), required=True)
    location = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': "input1"}), required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ImageForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'id': 'inputGroupFile02'}),
        required=True)


class DoctorForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={'class': "input1"}), required=True)
    location = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': "input1"}), required=True)
    fee = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': "input1"}), required=True)
