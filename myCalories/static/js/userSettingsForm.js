function getFormData() {
    let height = document.getElementById("height").value;
    let weight = document.getElementById("weight").value;
    let calories = document.getElementById("calories").value;
    let fat = document.getElementById("fat").value;
    let carbohydrates = document.getElementById("carbohydrates").value;
    let protein = document.getElementById("protein").value;
    let sex = document.getElementById("sex").value;
    let lang = document.getElementById("lang").value;

    if (height < 1 || weight < 1 || calories < 1 || fat < 1 || carbohydrates < 1 || protein < 1) {
        alertUserSettings();
        return;
    }

    $.ajax({
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "post/ajax/userSettingsForm",
        data: {'height': height,
                'weight': weight,
                'calories': calories,
                'fat': fat,
                'carbohydrates': carbohydrates,
                'protein': protein,
                'lang': lang,
                'sex': sex},
        success: function (response) {
            document.location.reload();
        },
        error: function () {
            alertUserSettings();
        }
    })
}