var mapDiv = document.getElementById("map");
var coordenadas = {lat: -33.03360822281903, lng:-71.53318410428794};
var map;
var marker;
function IniciarMapa(){
    map = new google.maps.Map(mapDiv, {
        center: coordenadas,
        zoom: 17
    });

    marker = new google.maps.Marker({
        position: coordenadas,
        map: map
    })
}