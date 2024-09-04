from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Contact
from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def validate_email(email):
    api_key = 'YOUR_API_KEY'
    response = requests.get(f'https://api.example.com/verify?email={email}&apikey={api_key}')
    result = response.json()
    
    # Check if the email is valid based on the response
    return result.get('status') == 'valid'


def homeView(request):
    if request.method == 'POST':
        yourname = request.POST.get('yourname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the data to the Contact model
        Contact.objects.create(
            yourname=yourname,
            email=email,
            subject=subject,
            message=message
        )
        return redirect("home")

    return render(request, 'index.html')
