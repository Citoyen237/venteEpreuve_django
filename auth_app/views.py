from django.shortcuts import render,redirect
from .utils import *
from .form import *
from django.contrib import messages
from .models import CustomUser as User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
import string
import random
# Create your views here.
def registerPage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():   
            last_name = form.cleaned_data.get('last_name')
            first_name = form.cleaned_data.get('first_name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=first_name,first_name=first_name,phone_number=phone,last_name=last_name, email=email, password=password)
            if user is not None :
                context = {'user': user}
                send_custom_email(
                 'Bienvenue sur notre site',
                 'emails/confirm_register.html',
                 context,
                 [email]
                )
                messages.success(request,'Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter')
                return redirect('auth.login')
            else:
                messages.error('erreur')
                return redirect('auth.register')
    else:
        form = RegisterForm()
    return render(request, 'registerPage.html', {'form': form})

def logoutPage(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('auth.login')

def loginPage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():   
           email = form.cleaned_data.get('email')
           password = form.cleaned_data.get('password')
           UserModel = get_user_model()
           try:
                user = UserModel.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, f'Bienvenue {user.first_name}!')
                    return redirect('front.index')  # Remplacez 'home' par le nom de l'URL de votre page d'accueil
                else:  
                    messages.error(request, 'Email ou mot de passe incorrect.')
           except UserModel.DoesNotExist:
                messages.error(request, 'Email ou mot de passe incorrect.')    
    else:
        form = LoginForm()
    return render(request, 'loginPage.html', {'form': form})

# class CustomLoginView(LoginView):
#     template_name = 'loginPage.html'
#     authentication_form = LoginForm

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
def forgetPassPage(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = generate_random_password()
                user.set_password(new_password)
                user.save()

                send_mail(
                    'Réinitialisation de votre mot de passe',
                    f'Votre nouveau mot de passe est : {new_password}',
                    'prodistributionltd@gmail.com',  # Remplacez par votre email
                    [email],
                    fail_silently=False,
                )

                messages.success(request, 'Un nouveau mot de passe a été envoyé à votre adresse email.')
                return redirect('auth.login')
            except User.DoesNotExist:
                messages.error(request, "Aucun utilisateur n'est associé à cet email.")
    else:
        form = PasswordResetForm()

    return render(request, 'forgetPassPage.html', {'form': form})