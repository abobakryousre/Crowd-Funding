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
    let category_id = JSON.parse(response['category_id'])
    let category_projects_location = document.getElementById('categories');
    category_projects_location.innerHTML = ` <h2 class="text-center mt-5 blue-header">
                                                     ${category_name} Projects</h2>
                                                    `;

    for (let index = 0; index < projects_toJson.length; index++) {
        insertProject(category_projects_location, projects_toJson[index].fields,projects_toJson[index].pk, project_images[index]);
    }

    category_projects_location.innerHTML += `<a  class="text-center col-md-3 btn btn-primary mt-2 mb-2 justify-content-center" href="/users/display-category?category_id=${category_id}">see all</a>\`
                                                    `;

}

function insertProject(location, project, project_pk, project_image) {

    location.innerHTML += `
            <div class="card col-md-1 me-3 mt-3 p-2" style="width: 15rem;">
                    <img src=" ${project_image} " class="card-img-top" style="height: 50%;" alt="...">
                    <div class="card-body">
                        <h5 class="card-title blue-text">${project.title}</h5>
                        <p class="card-text details-value">${project.details}</p>
                        <a href="projects/${project_pk}" class="btn btn-primary">More Details</a>
                    </div>
                </div>
            `
}

function submitQuery() {
    let query = document.getElementById('searchbar').value;
    let searchResultLocation = document.getElementById('search-result');

    // clear the search result location
    searchResultLocation.innerHTML = "";
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
        insertProject(searchResultLocation, projects[index].fields, projects[index].pk, project_images[index]);
    }
    let query = document.getElementById('searchbar').value;
    searchResultLocation.innerHTML += ` <a   class="text-center col-md-3 btn btn-primary mt-2 mb-2 justify-content-center" href="/projects/index?q=${query}">see all</a>`
    document.getElementById('searchbar').value = "";

}