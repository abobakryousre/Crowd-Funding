from django.contrib import messages
# from users.form import Usermodelform
from django.contrib.auth import authenticate, login, logout
# from users.forms import loginformauth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from users.forms import SignUpForm
# fun of registration
from users.models import User
from users.utils import account_activation_token


# Create your views here.

# fun of registration
def UserRegisterView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            ###############email activat##########################33
            user.is_active = False
            username = request.POST['username']
            email = request.POST['email']
            email_subject = 'Activate your account'
            current_site = get_current_site(request)
            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }

            link = reverse('activate', kwargs={
                'uidb64': email_body['uid'], 'token': email_body['token']})

            email_subject = 'Activate your account'

            activate_url = 'http://' + current_site.domain + link

            email = EmailMessage(
                email_subject,
                'Hi ' + ', Please the link below to activate your account \n' + activate_url,
                'crowedfunding@gmail.com',
                [email],
            )
            email.send(fail_silently=False)
            messages.success(request, 'Account successfully created')
            user.save()
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'users/form.html', context)

    form = SignUpForm()
    context = {'form': form}
    return render(request, 'users/form.html', context)


# log in fun
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Please Activate Your Account To Continue ')
        else:
            messages.info(request, 'Email or Password is Incorrect')

    return render(request, 'users/login.html')


# logout fun will used in bakr home page
def logoutUser(request):
    logout(request)
    return redirect('login')


class VerificationView(View):
    def get(self, request, uidb64, token):
        id = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=id)

        if user.is_active:
            messages.success(request, 'Account  already  Activated')
            return redirect('login')
        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong')
            return redirect('login')
