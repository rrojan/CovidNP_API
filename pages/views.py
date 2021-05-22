from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
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
        try:
            username = User.objects.get(email=email.lower()).username
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
            # verification_code = random.randint(1000, 9999)
            # subject = 'Welcome to The River Sweeps'
            # message = f'Your verification code is {verification_code}. Hope you enjoy your stay here!'
            # recepient = form.cleaned_data.get('email')
            # send_mail(subject, message, EMAIL_HOST_USER,
            #           [recepient], fail_silently=False)
            # form.save(code=verification_code)
            messages.success(request, "You have been signed up! You can now log in.")
            form.save()
            return redirect("index")
    messages.warning(request, "There was an error signing you up. Please try again.")
    return redirect("index")


def my_api_view(request):
    return render(request, "pages/my_api.html")
