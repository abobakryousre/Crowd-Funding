from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from users.form import Usermodelform
from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm
# from users.forms import loginformauth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

#fun of registration
def UserRegisterView(request):

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('frist_name')
            # messages.success(request, 'Account was created for ' + username)

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





