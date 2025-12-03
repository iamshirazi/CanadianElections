
function loadElection(electionYear) {
    window.location.href = "/elections/" + electionYear + ".html";
};

function loadAbout() {
    window.location.href = "/main/about.html";
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