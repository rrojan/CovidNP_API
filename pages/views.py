from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
from .forms import UserCreationForm


def index_view(request):
    context = {"signup_form": UserCreationForm()}
    return render(request, "pages/index.html", context)


def docs_view(request):
    return render(request, "pages/docs.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        print(email, password)
        try:
            username = User.objects.get(email=email.lower()).username
            print(username)
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return redirect("index")
        except Exception:
            messages.warning(request, "Wrong login credentials, please try again")
    return redirect("index")


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                # check if a user with that email already exists
                _ = User.objects.get(email = form.cleaned_data.get('email'))
                messages.warning(request, "An account with that email already exists. Please try logging in.")
            except Exception:
                pass
            verification_code = random.randint(1000, 9999)
            subject = 'Verify your CovidNP account'
            message = f'Your verification code is {verification_code}. Enter this verification code in your MyAPI to verify your account'
            recepient = form.cleaned_data.get('email')

            send_mail(subject, message, EMAIL_HOST_USER,
                      [recepient], fail_silently=False)

            form.save(code=verification_code)
            messages.success(request, "You have been signed up! You can now log in.")
            # form.save()
            return redirect("index")
    messages.warning(request, "There was an error signing you up. Please try again.")
    return redirect("index")

@login_required(redirect_field_name='my_api')
def my_api_view(request):
    context = {
        'user_token': Token.objects.get(user=request.user)
    }

    if request.method == "POST":
        code = request.POST.get('vcode')
        if request.user.profile.verification_code == int(code):
            request.user.profile.is_verified = True
            request.user.profile.save()
            messages.success(request, "Success! You can now use your account to query the CovidNP API")
        else:
            messages.warning(request, "Wrong verification code. Please try again")
        return redirect('my_api')

    return render(request, "pages/my_api.html", context)

def changelogs_view(request):
    return render(request, 'pages/changelogs.html')
