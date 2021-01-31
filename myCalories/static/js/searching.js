function foodSearcher(inp, arr) {
    let currentFocus;

    inp.addEventListener("input", function(e) {
        let a, b, i, val = this.value;

        closeAllLists();

        if (!val) { return false;}

        currentFocus = -1;
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(a);

      for (i = 0; i < arr.length; i++) {
        if (arr[i].substr(0, val.length).toUpperCase() === val.toUpperCase()) {
          b = document.createElement("DIV");
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";

          b.addEventListener("click", function(e) {
              inp.value = this.getElementsByTagName("input")[0].value;
              afterClick(inp.value);
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
    });

    inp.addEventListener("keydown", function(e) {
      let x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode === 40) {
        currentFocus++;
        addActive(x);

      } else if (e.keyCode === 38) {
        currentFocus--;
        addActive(x);

      } else if (e.keyCode === 13) {
        e.preventDefault();
        if (currentFocus > -1) {
          if (x) x[currentFocus].click();
        }
      }
    });

    function addActive(x) {
    if (!x) return false;

    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    x[currentFocus].classList.add("autocomplete-active");
    }

    function removeActive(x) {
        for (let i = 0; i < x.length; i++) {
          x[i].classList.remove("autocomplete-active");
        }
    }

    function closeAllLists(elmnt) {
      const x = document.getElementsByClassName("autocomplete-items");
      for (let i = 0; i < x.length; i++) {
          if (elmnt !== x[i] && elmnt !== inp) {
            x[i].parentNode.removeChild(x[i]);
          }
        }
    }

    document.addEventListener("click", function (e) {
      closeAllLists(e.target);
    });
}

const foods = [];
let userLang;

function downloadFoodList(lang){
    userLang = lang
    $.ajax({
    headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "/calories/post/ajax/allFoodList",
        success: function (response) {
            const foodList = JSON.parse(response['food_list']);

            foodList.forEach(function (food) {
                let foodString = "";
                if (lang === "en") {
                    foodString += food['name'];
                } else if (lang === "pl") {
                    foodString += food['name_pl'];
                }

                foods.push(foodString);
            })
        }
    })
}

function afterClick(foodName) {
    let food_unit = "undef";

    $.ajax({
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "/calories/post/ajax/getFood",
        data: {'lang': userLang,
                'food_name': foodName},
        success: function (response) {
            const food = JSON.parse(response['food']);
            food_unit = food['unit'];

            if (userLang === "pl" && food_unit === "pcs") food_unit = "szt";
            if (food_unit === "g") food_unit = " x100g";

            document.getElementById("unitOfAddFoodToDay").innerText = food_unit;

            document.getElementById("countOfAddFoodToDay").style.visibility = 'visible';
            document.getElementById("countOfAddFoodToDayLabel").style.visibility = 'visible';
            document.getElementById("unitOfAddFoodToDay").style.visibility = 'visible';
            document.getElementById("searcherButtons").style.visibility = 'visible';

        }
    })
}

function addFoodToDayFunction() {
    let foodName = document.getElementById("foodNameInput").value;
    let foodCount = document.getElementById("countOfAddFoodToDay").value;
    let date = document.getElementById('actualDate').innerHTML;

    if (isNaN(foodCount)) {
        alertNaN();
        return;
    }

    if (foodCount <= 0) {
        alertCountLessOrEqualZero();
        return;
    }

    $.ajax({
    headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "/calories/post/ajax/addFoodToDay",
        data: {'lang': userLang,
                'food_name': foodName,
                'count': foodCount,
                'date': date},
        success: function (response) {
            changeDate(date, userLang);
            hideSearcherFields();
        }
    })
}

function hideSearcherFields() {
    document.getElementById("countOfAddFoodToDay").style.visibility = 'hidden';
    document.getElementById("countOfAddFoodToDay").value= '';
    document.getElementById("countOfAddFoodToDayLabel").style.visibility = 'hidden';
    document.getElementById("unitOfAddFoodToDay").style.visibility = 'hidden';
    document.getElementById("searcherButtons").style.visibility = 'hidden';
    document.getElementById("foodNameInput").value = '';
}

foodSearcher(document.getElementById("foodNameInput"), foods)
