export const map = L.map("map").setView([60, -96], 4); // Canada center

import { retrieveDistrict } from "./elections_functions.js";

// Base layer
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© Matthew Shirazi",
}).addTo(map);

map.on("click", function () {
  const container = document.getElementById("searchResults");
  container.innerHTML = "";
});

function getPartyColour(party) {
  switch (party) {
    case "Liberal Party of Canada":
      return "#EE3224";
    case "Opposition":
      return "#EE3224";
    case "Conservative Party of Canada":
      return "#0F2D52";
    case "Progressive Conservative Party":
      return "#0F2D52";
    case "Conservative (1867-1942)":
      return "#0F2D52";
    case "Liberal-Conservative":
      return "#0F2D52";
    case "Unionist":
      return "#0F2D52";
    case "Unionist (Liberal)":
      return "#0F2D52";
    case "National Government":
      return "#0F2D52";
    case "Anti-Confederate":
      return "#F58220";
    case "Co-operative Commonwealth Federation":
      return "#F58220";
    case "New Democratic Party":
      return "#F58220";
    case "Labour":
      return "#FF8ADC";
    case "Nationalist Conservative":
      return "#800080";
    case "Nationalist":
      return "#800080";
    case "Patrons of Industry":
      return "#A52A2A";
    case "McCarthyite":
      return "#009A44";
    case "Progressive":
      return "#0DBA13";
    case "Liberal Progressive":
      return "#00DCB0";
    case "United Farmers of Alberta":
      return "#C0BD07";
    case "United Farmers of Ontario":
      return "#C0BD07";
    case "United Farmers of Ontario-Labour":
      return "#C0BD07";
    case "Reconstruction Party":
      return "#F5F5DC";
    case "Social Credit Party of Canada":
      return "#005F00";
    case "New Democracy":
      return "#005F00";
    case "Ralliement des créditistes":
      return "#005F00";
    case "United Reform Movement":
      return "#C00767";
    case "Unity":
      return "#C00767";
    case "Labor-Progressive Party":
      return "#C00767";
    case "Bloc populaire canadien":
      return "#00A7EC";
    case "Bloc Québécois":
      return "#00A7EC";
    case "Liberal Labour Party":
      return "#A91CB9";
    case "No affiliation to a recognised party":
      return "#000000";
    case "Green Party of Canada":
      return "#3D9B35";
    default:
      return "#cccccc";
  }
}

async function removeLoadingScreen() {
  const mapContainer = document.getElementById("mapContainer");
  const loadingSpinner = document.getElementById("loadingSpinner");

  mapContainer.style.opacity = "1";
  loadingSpinner.style.display = 'none';
}


async function loadDistricts() {
  const election_year = document.getElementById("current_election_text").textContent;
  const response = await fetch(`https://canadianelections.net/districts/geojson?election_year=${election_year}`);
  const data = await response.json();
  removeLoadingScreen();

  const layer = L.geoJSON(data, {
    style: function (feature) {
      return {
        fillColor: getPartyColour(feature.properties.party),
        weight: 1,
        color: "black",
        fillOpacity: 0.7
      };
    },
    onEachFeature: function (feature, layer) {
      layer.bindPopup(`
        <strong>${feature.properties.fedname}</strong>
      `);

      layer.on('click', function(e) {
        L.DomEvent.stopPropagation(e);

        retrieveDistrict(election_year, feature.properties.id);
      });

      layer.on('mouseover', function(e) {
        e.target.setStyle({
            fillOpacity: 0.9
        });
      });

      layer.on('mouseout', function(e) {
          e.target.setStyle({
              fillOpacity: 0.7
          });
      });

    }
  }).addTo(map);
  
  const bounds = layer.getBounds();
  map.fitBounds(bounds);
}

async function getParties() {
  const election_year = document.getElementById("current_election_text").textContent;
  const response = await fetch(`https://canadianelections.net/parties/?election_year=${election_year}`);
  const data = await response.json();


  const unordered_list = document.getElementsByClassName("legend-labels")[0];

  const parties = data.parties;

  parties.forEach(party => {

    const span_item = document.createElement('span');
    span_item.className = "legendPartySquares";
    span_item.style.backgroundColor = getPartyColour(party);

    const list_item = document.createElement('li');
    list_item.textContent = party;

    list_item.prepend(span_item);

    unordered_list.appendChild(list_item);
  })
  
}

loadDistricts();
getParties();
