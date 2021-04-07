function sendAjaxRequestToCheckPassword(password) {
    $.ajax({
        url: "/users/profile/check-password",
        type: "get",
        data: {
            password: password,
        },
        success: checkPasswordResponse
    });
}

function checkPasswordResponse(response) {
            if (response.isPasswordCorrect == true) {
                deleteAccount();
            } else {
                let error_message_location = document.getElementById(
                    "errors-message"
                );
                let error_message = document.createElement("p");
                error_message.textContent = "Password is not correct !";
                error_message_location.appendChild(error_message);
            }
        }

function checkPassword() {
    let password_field = document.getElementById("password");
    sendAjaxRequestToCheckPassword(password_field.value);
    clearTheModal();
}

function clearTheModal() {
    let error_message_location = document.getElementById("errors-message");
    error_message_location.innerHTML = "";
    let password_field = document.getElementById("password");
    password_field.value = "";
}

function deleteAccount() {
    let closeModalButton = document.getElementById("close-modal");
    let submitDeleteAccount = document.getElementById("submit-deleteAccount");
    closeModalButton.click();
    submitDeleteAccount.click();
}

let modal = document.getElementById("deleteAccount");
modal.addEventListener("hidden.bs.modal", clearTheModal());


