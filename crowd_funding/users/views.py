from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from users.form import Usermodelform
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View

from users.forms import SignUpForm
# from users.forms import loginformauth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

#fun of registration
from users.models import User
from users.utils import account_activation_token


def UserRegisterView(request):

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # username = form.cleaned_data.get('frist_name')
            # messages.success(request, 'Account was created for ' + username)
 ###############email activat##########################33
            user.is_active=False
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
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/form.html', context)

# log in fun
def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email OR password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)

#logout fun will used in bakr home page
def logoutUser(request):
    logout(request)
    return redirect('login')
# tried fun using temprary in home page to can render home url
def index(request):
    return HttpResponse("Hello world")


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')



