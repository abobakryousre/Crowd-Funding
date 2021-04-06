import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.shortcuts import render
from projects.models import Projects, Rating, Tags
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
    selected_project = Projects.objects.filter(selected=True)[:5];

    context = {
        'highest_projects': highest_rated_projects,
        'latest_projects': latest_five_projects,
        'categories': categories,
        'selected_projects': selected_project
    }
    return render(request, 'users/index.html', context)


def display_category(request):
    if request.is_ajax():
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
        return JsonResponse(
            {"projects": projectsModels_to_json, 'images': images_to_json, 'category_name': category_name})
    else:
        return HttpResponse("Page Not Found!");


def search_for_projects(request):
    if request.is_ajax():
        query = request.GET.get('query')
        # convert the query from string to array
        query = query.split(" ")
        if query == "@":
            all_projects = Projects.objects.all()
        else:
            all_matched_tags = Tags.objects.filter(tag_name__in=query)
            projects_by_tag = []
            if all_matched_tags:
                for tag in all_matched_tags:
                    projects_by_tag.append(tag.project)

            projects_by_title = Projects.objects.filter(title__in=query)

            # convert the query set to array
            all_projects = list(projects_by_tag) + list(projects_by_title)
            # remove the duplicated projects
            all_projects = list(dict.fromkeys(all_projects))

        # set projects image
        images = []
        for project in all_projects:
            image = project.images_set.first().path.url
            images.append(image)

        # convert Django Model Object to JSON string
        projects_models_to_json = serializers.serialize('json', all_projects, )
        images_to_json = json.dumps(images)
        return JsonResponse({"projects": projects_models_to_json, 'images': images_to_json})
    else:
        return HttpResponse("Page Not Found!");
