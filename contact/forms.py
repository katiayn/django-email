from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email")
    subject = forms.CharField(label="Subject", max_length=1000, required=False)
    message = forms.CharField(label="Massage", widget=forms.Textarea())
