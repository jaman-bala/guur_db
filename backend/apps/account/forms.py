from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "u-input u-input-rectangle"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "u-input u-input-rectangle"},
    ))