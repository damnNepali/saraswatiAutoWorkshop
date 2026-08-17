from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def index(request):
    """Single-page site: home, about, services, why-us, contact."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and phone:
            ContactMessage.objects.create(name=name, phone=phone, message=message_text)
            messages.success(request, "Thank you! We have received your message and will contact you soon.")
        else:
            messages.error(request, "Please fill in your name and phone number.")
        return redirect('/#contact')

    return render(request, 'workshop/index.html')
