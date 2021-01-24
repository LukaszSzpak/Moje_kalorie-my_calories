function addFoodManual(lang) {
    let foodName = document.getElementById("food_name_form").value;
    let foodCalories = document.getElementById("food_calories_form").value;
    let foodFat = document.getElementById("food_fat_form").value;
    let foodCarbohydrates = document.getElementById("food_carbohydrates_form").value;
    let foodProtein = document.getElementById("food_protein_form").value;
    let foodCount = document.getElementById("food_count_form").value;
    let foodUnit = document.getElementById("food_unit").value;
    let date = document.getElementById('actualDate').innerHTML;

    $.ajax({
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "post/ajax/addManualFoodToDay",
        data: {'lang': lang,
                'food_name': foodName,
                'food_calories': foodCalories,
                'food_fat': foodFat,
                'food_carbohydrates': foodCarbohydrates,
                'food_protein': foodProtein,
                'food_unit': foodUnit,
                'food_count': foodCount,
                'date': date},
        success: function (response) {
            changeDate(date, lang);
            clearManualFoodAdding();
            downloadFoodList(lang);
        }
    })

}

function clearManualFoodAdding() {
    document.getElementById("food_name_form").value = '';
    document.getElementById("food_calories_form").value = '';
    document.getElementById("food_fat_form").value = '';
    document.getElementById("food_carbohydrates_form").value = '';
    document.getElementById("food_protein_form").value = '';
    document.getElementById("food_count_form").value = '';
    document.getElementById("food_unit").value = '';
}