
function load1867Election() {
    document.getElementById('iframe').src = "../elections/election1867.html";
    document.getElementById('current_election_text').innerHTML = "1867"
};

function load2019Election() {
    document.getElementById('iframe').src = "../elections/election2019.html";
    document.getElementById('current_election_text').innerHTML = "2019"
};

function load2021Election() {
    document.getElementById('iframe').src = "../elections/election2021.html";
    document.getElementById('current_election_text').innerHTML = "2021"
};

function loadAbout() {
    document.getElementById('iframe').src = "./about.html";
    document.getElementById('current_election_text').innerHTML = ""
};