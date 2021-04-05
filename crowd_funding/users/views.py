from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from users.form import Usermodelform
from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm
# from users.forms import loginformauth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def UserRegisterView(request):

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'users/form.html', context)


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


def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    return HttpResponse("Hello world")





# def registerpage(request):
#     # render form
#     if request.method == 'GET':
#         form = createuserform()
#         context = {
#             'formregister': form
#         }
#         return render(request, 'users/form.html', context)
#
#         # check on data
#         # is valied => save data on database
#         # not => render form again
#     else:
#         fulldata = createuserform(request.POST, request.FILES)
#
#         if fulldata.is_valid():
#             fulldata.save()
#             # email=fulldata.cleaned_data('email')
#             # raw_password=fulldata.cleaned_data('password1')
#             # users=authenticate(email=email,passwor=raw_password)
#             # login(request,users)
#             return render(request,'users/home.html')
#         else:
#             context = {"formregister": fulldata}
#             return render(request, 'users/form.html', context)
#
#
# def loginform(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         user = authenticate(request, email=email, password=password)
#
#         if user is not None:
#             login(request, user)
#             return render('users/home.html')
#         else:
#             messages.info(request, 'Email OR password is incorrect')
#
#     context = {}
#     return render(request, 'users/login.html', context)

    ########################################
    # context = {}
    # if request.method == 'POST':
    #     print('loginnnnnnnnnn')
    #     form = loginformauth()
    #     context = {
    #         'formlogin': form
    #     }
    #     return render(request, 'users/login.html', context)
    # else:
    #     user = request.user
    #     if user.is_authenticated:
    #         print('uuuuuuseerr utttttttttttttttt')
    #
    #         return render(request, 'users/home.html')
    #     if request.POST:
    #         form = loginformauth(request.POST)
    #         if form.is_valid():
    #             email = request.POST['email']
    #             password = request.POST['password']
    #             user = authenticate(email=email, passwor=password)
    #             if user:
    #                 print('uuuuuuseerr')
    #                 login(request, user)
    #                 return render(request, 'users/home.html')
    #
    #
    #
