import os

from django.urls import reverse
from django.shortcuts import render, redirect

from contact.forms import ContactForm

import resend

resend.api_key = os.environ["RESEND_API_KEY"]
email_from = os.environ["RESEND_EMAIL_FROM"]


def thanks(request):
    return render(
        request=request,
        template_name='thanks.html'
    )


def contact_me(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            params = {
                "from": f"{data['name']} <{email_from}>",
                "to": f"{email_from}",
                "reply_to": f"{data['email']}",
                "subject": f"{data['subject']}" if data['subject'] else f"Hello from {data['name']}!",
                "text": f"{data['message']}",
            }
            resend.Emails.send(params)
            return redirect(reverse('contact:thanks'))
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
