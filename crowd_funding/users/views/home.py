import json
from django.core import serializers
from django.shortcuts import render, redirect
from projects.models import Projects, Rating
from projects.models.projects import Category
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # get the highest 5 rate
        highest_rate = Rating.objects.all().order_by('-five_star')[:5]
        highest_rated_projects = []
        for rate in highest_rate:
            highest_rated_projects.append(rate.project)
        # five-latest-projects
        latest_five_projects = Projects.objects.all().order_by('-created_at')[:5]
        categories = Category.objects.all()
        # list of 5 projects selected by admin
        selected_project = Projects.objects.filter(selected=True)[:5]
        context = {
            'highest_projects': highest_rated_projects,
            'latest_projects': latest_five_projects,
            'categories': categories,
            'selected_projects': selected_project,
        }
        return render(request, 'users/index.html', context)
    else:
        return redirect('login')


def display_category(request):
    if request.user.is_authenticated and request.is_ajax():
        category_id = request.GET.get('category_id')
        category = Category.objects.filter(pk=category_id)[0]
        projects = category.projects_set.all()
        # set projects image
        images = []
        for project in projects:
            image = project.images_set.first().path.url
            images.append(image)
        projectsModels_to_json = serializers.serialize('json', projects, )
        images_to_json = json.dumps(images)
        category_name = json.dumps(category.category_name)

        context = {
            "projects": projectsModels_to_json,
            'images': images_to_json,
            'category_name': category_name
        }
        return JsonResponse(context)
    else:
        return redirect('login')


def search_for_projects(request):
    if request.user.is_authenticated and request.is_ajax():
        query = request.GET.get('query')
        if query != "@":
            # convert the query from string separated with space  to array
            query = query.split(",")
            query = [q.lower() for q in query]
            all_projects = Projects.objects.filter(Q(tags__tag_name__in=query) | Q(title__in=query)).distinct()
        else:
            all_projects = Projects.objects.all()[:10]
        # set projects image
        images = []
        for project in all_projects:
            image = project.images_set.first().path.url
            images.append(image)

        # convert Django Model Object to JSON string
        projects_models_to_json = serializers.serialize('json', all_projects, )
        images_to_json = json.dumps(images)
        context = {
            "projects": projects_models_to_json,
            'images': images_to_json
        }
        return JsonResponse(context)
    else:
        return redirect('login')
