function displayCategoryProjects(category_id) {

    let category_projects_location = document.getElementById('categories');

    $.ajax({
        url: "/users/display-category",
        type: 'get',
        dataType: 'json',
        data: {
            'category_id': category_id
        },
        success: appendProjects
    });
}

function appendProjects(response) {
    let projects_toJson = JSON.parse(response['projects'])
    let project_images = JSON.parse(response['images']);
    let category_name = JSON.parse(response['category_name'])
    let category_projects_location = document.getElementById('categories');
    category_projects_location.innerHTML = ` <h2 class="text-center mt-5 " style="color: blue; font-weight: bold">
                                                     ${category_name} Projects</h2>
                                                    `;

    for (let index = 0; index < projects_toJson.length; index++) {
        insertProject(category_projects_location, projects_toJson[index].fields, project_images[index]);
    }

}

function insertProject(location, project, project_image) {
    location.innerHTML += `
            <div class="card col-md-1 me-3" style="width: 18rem;">
                    <img src=" ${project_image} " class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">${project.title}</h5>
                        <p class="card-text">${project.details}</p>
                        <a href="projects/${project.id}" class="btn btn-primary">More Details</a>
                    </div>
                </div>
            `
}

function submitQuery() {
    let query = document.getElementById('searchbar').value;
    let searchResultLocation = document.getElementById('search-result');

    // clear the search result location and the search bar
    searchResultLocation.innerHTML = "";
    document.getElementById('searchbar').value = "";

    if (query) {
        $.ajax({
            url: "/users/search-for-projects",
            type: 'get',
            dataType: 'json',
            data: {
                'query': query
            },
            success: appendSearchResult
        });
    }
}

function appendSearchResult(response) {
    let searchResultLocation = document.getElementById('search-result');
    let projects = JSON.parse(response['projects']);
    let project_images = JSON.parse(response['images']);
    for (let index = 0; index < projects.length; index++) {
        insertProject(searchResultLocation, projects[index].fields, project_images[index]);
    }
}