function calcAndAddFoodTableSum(foodList, lang) {
    let caloriesSum = 0;
    let fatsSum = 0;
    let carbohydratesSum = 0;
    let proteinsSum = 0;

    foodList.forEach(function (food) {
                let count = parseFloat(food["count"])

                caloriesSum += count * parseFloat(food["calories"]);
                fatsSum += count * parseFloat(food["fat"]);
                carbohydratesSum += count * parseFloat(food["carbohydrates"]);
                proteinsSum += count * food["protein"];
            })
    let tableSum = '<tr class="border_top"><td>';
    if (lang === "pl") tableSum += 'Suma:'; else tableSum += 'Sum:';
    tableSum += '</td><td>' + caloriesSum.toFixed(2) + 'kcal</td>' +
        '<td>' + fatsSum.toFixed(2) + 'g</td>' +
        '<td>' + carbohydratesSum.toFixed(2) + 'g</td>' +
        '<td>' + proteinsSum.toFixed(2) + 'g</td></tr>';

    document.getElementById("sums").innerHTML = tableSum;
}