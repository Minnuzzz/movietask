from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.shortcuts import redirect, render

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def save_profile(request):
    if request.method == 'POST':
        # Extract updated username and email from the form data
        updated_username = request.POST.get('username')
        updated_email = request.POST.get('email')

        # Update the user's information in the database
        user = request.user
        user.username = updated_username
        user.email = updated_email
        user.save()

        # Redirect back to the profile page
        return redirect('credentials:profile')
    else:
        # Handle invalid HTTP method
        return redirect('credentials:profile')  # Redirect to profile page or show error message


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('credentials:moviepage')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('credentials:login')
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return render(request, "index.html")
def moviepage(request):
    return render(request,'moviepage.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                                last_name=lastname)
                user.save()
                messages.success(request, 'You have registered successfully!')
                return redirect('credentials:login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('credentials:register')
    return render(request, 'index.html')

