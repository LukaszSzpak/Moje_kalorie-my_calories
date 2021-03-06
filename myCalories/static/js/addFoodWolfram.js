function addFoodWithWolfram(lang) {
    let foodName = document.getElementById("food_name_form_wolfram").value;
    let foodUnit = document.getElementById("food_unit_wolfram").value;
    let foodCount = document.getElementById("food_count_form_wolfram").value;
    let date = document.getElementById('actualDate').innerHTML;

    if (isNaN(foodCount)) {
        alertNaN();
        return;
    }

    if (foodCount <= 0) {
        alertCountLessOrEqualZero();
        return;
    }

    document.getElementById("loadingDiv").style.visibility = "visible";

    $.ajax({
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "post/ajax/addWolframFoodToDay",
        data: {'lang': lang,
                'food_name': foodName,
                'food_unit': foodUnit,
                'food_count': foodCount,
                'date': date},
        success: function (response) {
            changeDate(date, lang);
            clearWolframFoodAdding();
            downloadFoodList(lang);
        },
        error: function() {
              clearWolframFoodAdding();
              alertNotFoundWolfram();
        }
    })

}

function clearWolframFoodAdding() {
    document.getElementById("food_name_form_wolfram").value = '';
    document.getElementById("food_unit_wolfram").value = '';
    document.getElementById("food_count_form_wolfram").value = '';

    document.getElementById("loadingDiv").style.visibility = "hidden";
    document.getElementById("addNewWolfram").style.visibility = "hidden";
    document.getElementById("buttonsBelowTable").style.visibility = "visible";
}