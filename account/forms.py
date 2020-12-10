from django import forms

class name(forms.Form):
        username = forms.CharField(label='Username', max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','autofocus':'autofocus','name':'username'}))

class passw(forms.Form):
        password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autofocus':'autofocus','name':'password'}))

class passw1(forms.Form):
        password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autofocus':'autofocus','name':'password1'}))

class passw2(forms.Form):
        password = forms.CharField(label='Confirm password', max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password','autofocus':'autofocus','name':'password2'}))
