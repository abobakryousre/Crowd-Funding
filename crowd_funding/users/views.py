from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from .models import User
from .forms import UserProfile
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'users/index.html')


def edit_profile(request):
    if request.method == "GET":
        # will replace static user_id with the current_user id like -> request.user.pk
        user_id = User.objects.first().pk
        current_user = User.objects.get(pk=user_id)
        user_profile = UserProfile(instance=current_user)
        # is there any checks here ?
        context = {"user_profile": user_profile}
        return render(request, "users/edit_profile.html", context)
    else:
        user_id = User.objects.first().pk
        current_user = User.objects.get(pk=user_id)
        updated_data = UserProfile(request.POST, request.FILES, instance=current_user)
        if updated_data.is_valid():
            updated_data.save()
            return redirect('index')
        else:
            context = {"user_profile": updated_data}
            return render(request, "users/edit_profile.html", context)


def view_profile(request):
    # get user information
    current_user = User.objects.first()  # will change with request.usr.pk
    context = {"current_user": current_user}
    return render(request, 'users/profile.html', context)


def check_password(request):
    if request.is_ajax():
        password = request.GET.get("password");
        user = User.objects.first()
        if user.password == password:
            return JsonResponse({"isPasswordCorrect": True})
        else:
            return JsonResponse({"isPasswordCorrect": False})
    else:
        return HttpResponse("Page Not Found!");
def delete_account(request):
    return render(request, 'users/index.html')