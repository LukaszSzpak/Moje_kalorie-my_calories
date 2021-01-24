function getFormData() {
    let height = document.getElementById("height").value;
    let weight = document.getElementById("weight").value;
    let calories = document.getElementById("calories").value;
    let fat = document.getElementById("fat").value;
    let carbohydrates = document.getElementById("carbohydrates").value;
    let protein = document.getElementById("protein").value;
    let sex = document.getElementById("sex").value;
    let lang = document.getElementById("lang").value;

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
        }
    })
}