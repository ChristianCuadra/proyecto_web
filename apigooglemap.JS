var storedLat = localStorage.getItem('lat');
var storedLong = localStorage.getItem('lng');

if(storedLat&&storedLong){
    obtenerCoordenadas(JSON.parse(storedLat));
    obtenerCoordenadas(JSON.parse(storedLong));
}else{
    fetch('https://maps.googleapis.com/maps/api/geocode/json?address=ViñaDelMar&key=AIzaSyDnJ7HU3CttyubCqebQz5aVPMKZVmCybWI')
    .then(Response=>Response.json)
    .then(data=>{
        localStorage.setItem('lat', JSON.stringify(data));
        localStorage.setItem('lng', JSON.stringify(data));
        obtenerCoordenadas(data);
    })
    .catch(error => console.error('Error fetching data:', error));
}
function obtenerCoordenadas(data){
    var latitud = data.results.geometry[0][0];
    var longitud = data.results.geometry[1][1];

}

var mapDiv = document.getElementById("map");
var map;
var marker;
function IniciarMapa(){
    map = new google.maps.Map(mapDiv, {
        center: storedLat, storedLong ,
        zoom: 17
    });

    marker = new google.maps.Marker({
        position: storedLat, storedLong,
        map: map
    })
}