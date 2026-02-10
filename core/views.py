from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # ارسال ایمیل (اختیاری)
            # send_mail(...)
            sent = True
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form, "sent": sent})
