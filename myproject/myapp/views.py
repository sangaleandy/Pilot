from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django_daraja.mpesa.core import MpesaClient

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
    #cl = MpesaClient()
    #phone_number = '0702977498'
    #amount = 1000
    #account_reference = 'reference'
    #transaction_desc = 'Description'
    #callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    #response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    #return HttpResponse(response)

def counter(request):
    text = request.POST['text']
    return render(request, 'counter.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
            
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('index')

        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('/')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def stk_push_callback(request):
    data = request.body

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')