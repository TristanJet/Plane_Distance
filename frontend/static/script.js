// Create the map
const map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Load your custom GeoJSON region
fetch("data/custom.geo.json")
  .then(res => res.json())
  .then(geojson => {
    const layer = L.geoJSON(geojson).addTo(map);
    map.fitBounds(layer.getBounds()); // zoom map to border
  });

const pointA = [60.173, 24.941];
const pointB = [62.242, 25.748];

const mA = L.marker(pointA).addTo(map);
const mB = L.marker(pointB).addTo(map);