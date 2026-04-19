import { map } from "./map_template.js";

///// EventListeners FOR CLICKING ON THE 1867 AND NEWEST ELECTION BUTTONS /////
const election1867 = document.getElementById("button1867");
const newestElection = document.getElementById("newestElection");
const closeButton = document.getElementById("closeTableButton");

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


///// EventListener FOR PARLIAMENT CHART BUTTON /////
const parliamentChartButton = document.getElementById("parliamentChartButton");

export function set_parliament_chart(electionYear) {
    const parl_chart = document.getElementById('parliamentChart')
    const html_file = "../main/parliament_charts/parl_chart" + electionYear + ".html"

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

export function toggle_parliament_chart() {
    const parl_chart = document.getElementById('parliamentChart')

    if (parl_chart.style.display === "none") {
        parl_chart.style.display = "block";
    } else {
        parl_chart.style.display = "none";
    }
}

parliamentChartButton.addEventListener("click", (event) => {
    toggle_parliament_chart();
});

window.addEventListener('load', set_parliament_chart(document.getElementById("current_election_text").textContent));
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


///// EventListener FOR SEARCH BAR /////
const searchBar = document.getElementById("searchBar");

export function search(election_year) {
    var candidateOrDistrict = document.getElementById("searchBar").value;

    if (candidateOrDistrict != null && isNaN(candidateOrDistrict)) {

        fetch(`https://canadianelections.net/search?query=${candidateOrDistrict}&election_year=${election_year}`)
        .then(res => res.json())
        .then(data => {
            renderSearchResults(data);
        });
    }
    else {
        const container = document.getElementById("searchResults");
        container.innerHTML = "";
        closeButton.style.display = "none";
    }
}

searchBar.addEventListener("keyup", (event) => {
    const election_year = document.getElementById("current_election_text").textContent;

    search(election_year);
});
//////////////////////////////////// END /////////////////////////////////////////


///// EventListener FOR THE LEGEND /////
const legend = document.getElementById("legend");

export function collapseLegend() {
    const legendScale = document.querySelector(".legend-scale");
    legendScale.classList.toggle("collapsed");

    if (legendScale.style.visibility == "hidden") {
        legendScale.style.visibility = "hidden";
    } else {
        legendScale.style.visibility = "visible";
    }
};

legend.addEventListener("click", (event) => {
    collapseLegend();
});
//////////////////////////////////// END /////////////////////////////////////////


export async function zoomToDistrict_with_CandidateID(electionId, candidateId) {
    const response = await fetch(`https://canadianelections.net/districts/${electionId}/${candidateId}/geojson`);
    const feature = await response.json();
    const container = document.getElementById("searchResults");
    const election_year = document.getElementById("current_election_text").textContent;

    const templayer = L.geoJSON(feature);

    map.fitBounds(templayer.getBounds());

    // CLEAR SEARCH RESULTS IN TABLE
    container.innerHTML = "";
    closeButton.style.display = "none";
    clearInput();
    retrieveDistrict(election_year, feature.features[0].properties.id);
}


export async function zoomToDistrict(districtId) {
    const response = await fetch(`https://canadianelections.net/districts/${districtId}/geojson`);
    const feature = await response.json();
    const container = document.getElementById("searchResults");
    const election_year = document.getElementById("current_election_text").textContent;

    const templayer = L.geoJSON(feature);

    map.fitBounds(templayer.getBounds());

    // CLEAR SEARCH RESULTS IN TABLE
    container.innerHTML = "";
    closeButton.style.display = "none";
    clearInput();
    retrieveDistrict(election_year, districtId);
}


function clearInput() {
    document.getElementById('searchBar').value = '';
}


export function retrieveDistrict(election_year, districtId) {

    if (districtId != null) {

        fetch(`https://canadianelections.net/districts/${districtId}/results?election_year=${election_year}`)
        .then(res => res.json())
        .then(data => {
            renderResultsTable(data);
        });
    }
}

///// EventListener FOR THE X BUTTON TO CLOSE THE results-table /////
function closeResultsTable(event) {
    const container = document.getElementById("searchResults");
    container.innerHTML = "";
    closeButton.style.display = "none";
};
    
closeButton.addEventListener("click", closeResultsTable);
//////////////////////////////////// END /////////////////////////////////////////


function renderResultsTable(data) {
    const container = document.getElementById("searchResults");

    const results = data.results;
    
    // CLEAR PREVIOUS RESULTS
    container.innerHTML = "";

    if (!results || results.length === 0) {
        // RETURN NOTHING!
        return;
    }

    // MAKE X BUTTON ON TABLE VISIBLE
    closeButton.style.display = "inline-block";

    const table = document.createElement("table");
    table.className = "results-table";

    // HEADERS
    const ridingHeader = document.createElement("thead");
    ridingHeader.id = "ridingHeader";
    ridingHeader.innerHTML = `
        <tr>
            <th colspan="5">${data.district}</th>
        </tr>
    `;
    table.appendChild(ridingHeader);

    const thead = document.createElement("thead");
    thead.id = "districtResultsColumns";
    thead.innerHTML = `
        <tr>
            <th>Candidate</th>
            <th>Party</th>
            <th>Occupation</th>
            <th>Votes</th>
            <th>Result</th>
        </tr>
    `;
    table.appendChild(thead);

    // BODY
    const tbody = document.createElement("tbody");

    results.forEach(row => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${row.candidate}</td>
            <td>${row.party}</td>
            <td>${row.occupation}</td>
            <td>${row.votes.toLocaleString()}</td>
            <td>${row.result}</td>
        `;
        tbody.appendChild(tr);
    });

    table.appendChild(tbody);
    container.appendChild(table);

    updateScrollFade();
}


function renderSearchResults(results) {
    const election_year = document.getElementById("current_election_text").textContent;
    const container = document.getElementById("searchResults");

    // CLEAR PREVIOUS RESULTS
    container.innerHTML = "";
    closeButton.style.display = "none";

    if (!results || results.length === 0) {
        container.textContent = "No results found.";
        return;
    }

    const table = document.createElement("table");
    table.className = "results-table";

    // HEADER
    const thead = document.createElement("thead");
    thead.className = "searchResultsColumns";
    thead.innerHTML = `
        <tr>
            <th>Name</th>
            <th>Type</th>
        </tr>
    `;
    table.appendChild(thead);

    // BODY
    const tbody = document.createElement("tbody");

    results.candidates.forEach(row => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${row.name}</td>
            <td>candidate</td>
        `;
        tbody.appendChild(tr);
        tr.addEventListener("click", () => {
            zoomToDistrict_with_CandidateID(election_year, row.id);
        });
    });

    results.districts.features.forEach(row => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${row.properties.fedname}</td>
            <td>district</td>
        `;
        tbody.appendChild(tr);
        tr.addEventListener("click", () => {
            zoomToDistrict(row.properties.id);
        });
    });

    table.appendChild(tbody);
    container.appendChild(table);

    updateScrollFade();
}

const container = document.getElementById("searchResults");

container.addEventListener("scroll", () => {
    if (container.scrollTop > 0) {
        container.classList.add("scrolled");
    } else {
        container.classList.remove("scrolled");
    }

    /// IF SCROLLED TO THE BOTTOM OF TABLE, HIDE MASK-IMAGE GRADIENT
    const atBottom =
        container.scrollHeight - container.scrollTop <= container.clientHeight + 1;

    container.classList.toggle("at-bottom", atBottom);

});


function updateScrollFade() {
    const container = document.getElementById("searchResults");

    if (container.scrollHeight > container.clientHeight) {
        container.classList.add("scrollable");
    } else {
        container.classList.remove("scrollable");
    }
}
