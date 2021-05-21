from django.shortcuts import render
# from .forms import UserCreationForm, VerificationForm, RedeemRequestForm
from django.core.mail import send_mail


def index_view(request):
    return render(request, "pages/index.html", context={})


def docs_view(request):
    return render(request, "pages/docs.html", context={})

# def signup_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data.get('email'))

#             verification_code = random.randint(1000, 9999)
#             subject = 'Welcome to The River Sweeps'
#             message = f'Your verification code is {verification_code}. Hope you enjoy your stay here!'
#             recepient = form.cleaned_data.get('email')
#             send_mail(subject, message, EMAIL_HOST_USER,
#                       [recepient], fail_silently=False)
#             form.save(code=verification_code)
#             # user.profile.verification_code = verification_code
#             # print(user.profile)
#             return redirect('blogs:signup_success')

#     context = {
#         'form': UserCreationForm()
#     }

#     return render(request, 'signup/signup.html', context)