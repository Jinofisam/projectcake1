from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse


from .models import cakeorder
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import orders



def home_page(request):
    return render(request, 'home_page.html')

def home(request):
    return render(request, 'home.html')




def sign_up(request):
    return render(request, 'sign_up.html')

def order1(request):
    return render(request, 'order1.html')
def order2(request):
    return render(request, 'order2.html')
def order3(request):
    return render(request, 'order3.html')
def order4(request):
    return render(request, 'order4.html')
def order5(request):
    return render(request, 'order5.html')


def ordersave(request):
    if request.method == "POST":
        cake_name = request.POST.get('cake_name')
        price = request.POST.get('price')
        form = orders(request.POST)
        
        if form.is_valid():
            order = form.save(commit=False)
            order.cake_name = cake_name
            order.price = price
            order.save()
            return redirect('/ordered')
        else:
            return redirect('/order1')
    else:
        form = orders()
        return render(request, 'order1.html', {'form': form})

def ordered(request):
    last_order = cakeorder.objects.latest('id')  
    total_price = last_order.quantity * last_order.price  
    return render(request, 'ordered.html', {'users': [last_order], 'total_price': total_price})

def chocolate_cake_order(request):
    return redirect('order1') 

def vanilla_cake_order(request):
    return redirect('order2') 

def Icing_cake_order(request):
    return redirect('order3') 

def Cup_cakes_order(request):
    return redirect('order4') 

def Mirror_Glaze_cake_order(request):
    return redirect('order5') 

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# SignUp View
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                return redirect('home')  
            else:
                
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
        else:
            
            return render(request, 'login.html', {'form': form, 'error': 'Please correct the errors below.'})
    else:
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form})



def home_view(request):
    return render(request, 'home_page.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request) 
    return redirect('login')  
