from django.shortcuts import render, redirect

# Create your views here.



from django.http import HttpResponse
from projects.models import Projects, Images
from projects.models.projects import Donation
from django.db.models import Sum


def index(request):

    projects_of_specific_user = Projects.objects.filter(user_id = 1)
    donations=Donation.objects.select_related('project').filter(user_id=1)


    return render(request, 'users/profile.html',{"projects":projects_of_specific_user,"donations":donations})



def deleteItem(request,pk):
    sum_donations_of_project = Donation.objects.values('project_id').order_by('project_id').annotate(total_price=Sum('amount')).get(project_id=pk)

    project = Projects.objects.get(id=pk)

   # return HttpResponse(str(project.total_target))
    if sum_donations_of_project["total_price"] >= project.total_target*(25/100):

        return HttpResponse("Sorry,You can't delete this project because its donations exceeds 25% of total target")

    else:
        project.delete()
        return HttpResponse("Done")













