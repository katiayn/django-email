from django.urls import path

from .views import contact_me, thanks

app_name = 'contact'

urlpatterns = [
    path('contact-me/', contact_me, name='contact_me'),
    path('thanks/', thanks, name='thanks'),
]