
function loadElection(electionYear) {
    document.getElementById('iframe').src = "/elections/election" + electionYear + ".html";
    document.getElementById('current_election_text').innerHTML = electionYear
    set_parliament_chart(electionYear)
    display_parliament_chart_button()
    hideDropdownMenu()
};

function loadAbout() {
    document.getElementById('iframe').src = "/main/about.html";
    document.getElementById('current_election_text').innerHTML = ""
    hide_parliament_chart_button()
};

function set_parliament_chart(electionYear) {
    const parl_chart = document.getElementById('parliamentChart')
    const html_file = "/main/parliament_charts/parl_chart" + electionYear + ".html"

    fetch(html_file)
        .then(res => {
            if (res.ok) {
                return res.text();
            }
        })
        .then(htmlContent => {
            parl_chart.innerHTML = htmlContent
        })
}

function toggle_parliament_chart() {
    const parl_chart = document.getElementById('parliamentChart')

    if (parl_chart.style.display === "none") {
        parl_chart.style.display = "block";
    } else {
        parl_chart.style.display = "none";
    }
}

function display_parliament_chart_button() {
    const parl_chart_button = document.getElementById('parliamentChartButton')

    if (parl_chart_button.style.display != "flex") {
        parl_chart_button.style.display = "flex";
    }
}

function hide_parliament_chart_button() {
    const parl_chart_button = document.getElementById('parliamentChartButton')
    const parliamentChart = document.getElementById('parliamentChart')

    parl_chart_button.style.display = "none";
    parliamentChart.style.display = "none";
    
}

function showDropdownMenu() {
    const dropdownContent = document.querySelector('.dropdown-content');

    dropdownContent.style.display = "block";
}

function hideDropdownMenu() {
    const dropdownContent = document.querySelector('.dropdown-content');

    dropdownContent.style.display = "none";
}

document.addEventListener('click', function(event) {
    const dropdownContent = document.querySelector('.dropdown-content');
    const moreButton = document.getElementById('moreButton')
    
    if (dropdownContent && !dropdownContent.contains(event.target) && (event.target !== dropdownContent && event.target !== moreButton)) {
        dropdownContent.style.display = 'none';
    }
});