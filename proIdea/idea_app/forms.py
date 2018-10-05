from django import forms

# get email
class Sharing(forms.Form):
	email = forms.EmailField()