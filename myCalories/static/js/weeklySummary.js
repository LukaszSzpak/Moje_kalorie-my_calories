function parseWeeklyData(newWeek, lang) {
    $.ajax({
        headers: {"X-CSRFToken": Cookies.get('csrftoken')},
        type: 'POST',
        url: "post/ajax/weeklySummary",
        data: {'date': newWeek},
        success: function (response) {
            const prev_week = response['prev_week'];
            const act_week = response['act_week'];
            const next_week = response['next_week'];

            document.getElementById('prev_week').innerHTML = prev_week[0] + ' - ' + prev_week[6];
            document.getElementById('prev_week').onclick = function () {parseWeeklyData(prev_week[0], lang)};

            document.getElementById('act_week').innerHTML = act_week[0] + ' - ' + act_week[6];

            document.getElementById('next_week').innerHTML = next_week[0] + ' - ' + next_week[0];
            document.getElementById('next_week').onclick = function () {parseWeeklyData(next_week[0], lang)};
        }
    })
}
