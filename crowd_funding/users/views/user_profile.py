from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.db.models import Sum
from django.http import Http404, JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from projects.models import Donation, Images, Projects

from users.forms import UserProfile
from users.models import User

# from projects.models.projects import Donation

# Create your views here.

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            user_profile = UserProfile(instance=request.user)
            context = {"user_profile": user_profile}
            return render(request, "users/edit_profile.html", context)
        else:
            updated_data = UserProfile(request.POST, request.FILES, instance=request.user)
            if updated_data.is_valid():
                updated_data.save()
                return redirect('profile')
            else:
                context = {"user_profile": updated_data}
                return render(request, "users/edit_profile.html", context)
    else:
        return redirect('login')

def view_profile(request):
    if request.user.is_authenticated:
        # get user information
        projects_of_specific_user = Projects.objects.filter(user_id = request.user.pk)
        donations=Donation.objects.select_related('project').filter(user_id= request.user.pk)

        context = {
        "projects":projects_of_specific_user,
        "donations":donations
        }

        return render(request, 'users/profile.html', context)
    else:
        return redirect('login')


def check_password(request):
    # check password before  delete the account
    if  request.user.is_authenticated and request.is_ajax():
        password = request.GET.get("password");
        user = authenticate(request, email=request.user.email, password=password)
        if user is not None:
            return JsonResponse({"isPasswordCorrect": True})
        else:
            return JsonResponse({"isPasswordCorrect": False})
    else:
        return redirect('login')


def delete_account(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        user.delete()
        return redirect('login')
    else:
        return redirect('login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'users/change_password.html')
        else:
            current_user = User.objects.get(pk=request.user.pk)
            user = authenticate(request, email=request.user.email, password=request.POST.get('old-password'))
            if user is not None:
                if request.POST.get('password1') == request.POST.get('password2'):
                    current_user.set_password( request.POST.get("password1") )
                    current_user.save()
                    update_session_auth_hash(request, current_user)
                    return redirect('profile')
                else:
                    context = {'error': "New Passwords Not match"}
                    return render(request, 'users/change_password.html', context)
            else:
                context = {'error': "Old Passwords Incorrect"}
                return render(request, 'users/change_password.html', context)
    else:
        return redirect('login')

def deleteItem(request,pk):
    if request.user.is_authenticated:
        project = Projects.objects.get(id=pk)
        try:
            sum_donations_of_project = Donation.objects.values('project_id').order_by('project_id').annotate(
                total_price=Sum('amount')).get(project_id=pk)

            if sum_donations_of_project["total_price"] >= project.total_target * (25 / 100):

               return redirect('user-projects')

        except Donation.DoesNotExist:
            project.delete()
            return redirect('user-projects')
    else:
        return redirect('login')


def show_user_projects(request):
    if request.user.is_authenticated:
        projects_of_specific_user = Projects.objects.filter(user_id= request.user.pk)

        context = {
                   "projects": projects_of_specific_user,

                   }

        return render(request, 'users/projects_of_user.html', context)
    else:
        return redirect('login')

def show_user_donations(request):
    if request.user.is_authenticated:
        donations = Donation.objects.select_related('project').filter(user_id=request.user.pk)
        context = {
                   "donations": donations
                   }
        return render(request, 'users/donations_of_user.html', context)
    else:
        return redirect('login')