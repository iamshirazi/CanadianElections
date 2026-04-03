///// EventListeners FOR CLICKING ON THE 1867 AND NEWEST ELECTION BUTTONS /////
const election1867 = document.getElementById("button1867");
const newestElection = document.getElementById("newestElection");

election1867.addEventListener("click", (event) => {
    loadElection(election1867.textContent);
});

newestElection.addEventListener("click", (event) => {
    loadElection(newestElection.textContent);
});
//////////////////////////////////// END /////////////////////////////////////////


///// EventListener FOR THE ABOUT BUTTON /////
const aboutButton = document.getElementById("aboutButton");

export function loadAbout() {
    window.location.href = "/main/about.html";
};

aboutButton.addEventListener("click", (event) => {
    loadAbout();
});
//////////////////////////////////// END /////////////////////////////////////////


///// EventListener FOR THE "MORE" BUTTON (DROPDOWN MENU) /////
const moreButton = document.getElementById("moreButton");

export function toggleDropdownMenu() {
    const dropdownContent = document.querySelector('.dropdown-content');

    if (dropdownContent.style.display == "none") {
        dropdownContent.style.display = "block";
    } else {
        dropdownContent.style.display = "none";
    }
}

moreButton.addEventListener("click", (event) => {
    toggleDropdownMenu();
});

document.addEventListener('click', function(event) {
    const dropdownContent = document.querySelector('.dropdown-content');
    const moreButton = document.getElementById('moreButton');

    // IF DROPDOWN MENU WAS NOT CLICKED, AND THE MORE BUTTON WAS NOT CLICKED, HIDE THE DROPDOWN MENU
    if (dropdownContent && !dropdownContent.contains(event.target) && (event.target !== dropdownContent && event.target !== moreButton)) {
        dropdownContent.style.display = 'none';
    }
});
//////////////////////////////////// END /////////////////////////////////////////


///// EventListener FOR ALL BUTTONS IN THE DROPDOWN MENU
const dropdownButtons = document.querySelectorAll('.dropdown-content'); //

export function loadElection(electionYear) {
    window.location.href = "/elections/" + electionYear + ".html";
};

dropdownButtons.forEach(button => {

    button.addEventListener('click', (event) => { //
        loadElection(event.target.textContent);
    });
});
//////////////////////////////////// END /////////////////////////////////////////
