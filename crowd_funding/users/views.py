import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.shortcuts import render
from projects.models import Projects, Rating
from projects.models.projects import Category
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    # TODO: slider, for highest 5 reated projects
    # get the highest 5 rate
    highest_rate = Rating.objects.all().order_by('-five_star')[:5]
    highest_rated_projects = []
    for rate in highest_rate:
        highest_rated_projects.append(rate.project)
    # TODO: five-latest-projects
    latest_five_projects = Projects.objects.all().order_by('-created_at')[:5]
    # TODO: list of 5 projects selected by admin
    # TODO: each category and display  it's projects with ajax request
    categories = Category.objects.all()
    # TODO: search bar, with projects tag, and title.
    context = {
        'highest_projects': highest_rated_projects,
        'latest_projects': latest_five_projects,
        'categories': categories
    }
    return render(request, 'users/index.html', context)


def display_category(request):
    if request.is_ajax():
        category_id = request.GET.get('category_id')
        category = Category.objects.filter(pk=category_id)[0]
        projects = category.projects_set.all()
        projectsModels_to_json =  serializers.serialize('json', projects,)

        return JsonResponse({"projects": projectsModels_to_json})
    else:
        return HttpResponse("Page Not Found!");
