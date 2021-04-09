function checkDonation(project_id) {

    $.ajax({
        url: "/users/delete-project/",
        type: 'get',
        data: {
            'project_id': project_id
        },
        success: checkDonationResponse
    })
}

function checkDonationResponse(response) {
    if (response['deleted'] == false) {
        alert("Sorry You Can't Delete The Project, The project Donation is more than 25%");
    } else {
        alert("Project Deleted Successfully");
        window.location.href = "/users/profile/my-projects";
    }
}