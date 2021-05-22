from django import forms

class FormName(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)