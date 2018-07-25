from django import forms
from captcha.fields import CaptchaField
class loginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=128)
    password = forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput)
    usertype = forms.CharField(label='类型',max_length=20)
    captcha = CaptchaField(label='验证码')