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
                table += '<tr>'

                if (lang === "pl") {
                    table += '<td>' + food["name_pl"] + '</td>';
                } else if (lang === "en") {
                    table += '<td>' + food["name"] + '</td>';
                }

                table += '<td>' + food["calories"] + 'kcal</td>' +
                '<td>' + food["fat"] + 'g</td>' +
                '<td>' + food["carbohydrates"] + 'g</td>' +
                '<td>' + food["protein"] + 'g</td>' +
                '<td>' + food["count"] + food["unit"] +'</td>' +
                '</tr>';
            })
            document.getElementById('foods').innerHTML = table;

            document.getElementById('prev_date').innerHTML = response['prev_date'];
            document.getElementById('prev_date').onclick = function () {changeDate(response['prev_date'], lang)};

            document.getElementById('act_date').innerHTML = response['act_date'];
            document.getElementById('actualDate').innerHTML = response['act_date'];
            document.getElementById('act_date').onclick = function () {changeDate(response['act_date'], lang)};

            document.getElementById('next_date').innerHTML = response['next_date'];
            document.getElementById('next_date').onclick = function () {changeDate(response['next_date'], lang)};
        }
    })
}
