
function loadElection(electionYear) {
    document.getElementById('iframe').src = "/elections/election" + electionYear + ".html";
    document.getElementById('current_election_text').innerHTML = electionYear
};

function loadAbout() {
    document.getElementById('iframe').src = "/main/about.html";
    document.getElementById('current_election_text').innerHTML = ""
};