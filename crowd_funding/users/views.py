from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


from users.forms import SignUpForm

# Create your views here.

#fun of registration
def UserRegisterView(request):


    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('login')

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
