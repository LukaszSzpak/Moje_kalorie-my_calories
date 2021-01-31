function changeDate(newDate, lang) {
    $.ajax({
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "/calories/post/ajax/dayFoodList",
        data: {'date': newDate},
        success: function (response) {
            const food_list = JSON.parse(response['food_list']);
            let table = '';

            food_list.forEach(function (food) {
                let unit_var = '';
                if (food["unit"] === "pcs"){
                    if (lang === "pl") {
                        unit_var = "szt";
                    } else {
                        unit_var = "pcs";
                    }

                } else {
                    unit_var = "100g";
                }

                table += '<tr>'
                if (lang === "pl") {
                    table += '<td>' + food["name_pl"] + '</td>';
                } else if (lang === "en") {
                    table += '<td>' + food["name"] + '</td>';
                }
                table += '<td><p class="before_unit">' + food["calories"] + 'kcal</p><p class="unit_small"> /' + unit_var + '</p></td>' +
                '<td><p class="before_unit">' + food["fat"] + 'g</p><p class="unit_small"> /' + unit_var + '</p></td>' +
                '<td><p class="before_unit">' + food["carbohydrates"] + 'g</p><p class="unit_small"> /' + unit_var + '</p></td>' +
                '<td><p class="before_unit">' + food["protein"] + 'g</p><p class="unit_small"> /' + unit_var + '</p></td>' +
                '<td><p class="before_unit">';

                if (food["unit"] === 'g') {
                    table += food["count"] * 100;
                    table += 'g';
                } else {
                    table += food["count"] + unit_var;
                }
                table += '</p></td>' + '</tr>';
            })

            calcAndAddFoodTableSum(food_list, lang);
            document.getElementById('foods').innerHTML = table;

            document.getElementById('prev_date').innerHTML = response['prev_date'];
            document.getElementById('prev_date').onclick = function () {changeDate(response['prev_date'], lang)};

            document.getElementById('actualDate').innerHTML = response['act_date'];

            document.getElementById('next_date').innerHTML = response['next_date'];
            document.getElementById('next_date').onclick = function () {changeDate(response['next_date'], lang)};
        }
    })
}
