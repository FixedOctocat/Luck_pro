ymaps.ready(init);
var myMap, myGeoObject, myRectangle;

function init () {
    var coffw = 200
    var coffh = 100
    myMap = new ymaps.Map('map',{center: [55.753960, 37.620393],zoom: 12},{searchControlProvider: 'yandex#search'});
    for(var i1 = 11114; i1 <= 11180; i1++){
        console.log(i1);
        for(var i2 = 3737; i2 <= 3783; i2++){
            console.log(i2);
            myMap.geoObjects.add(new ymaps.Rectangle([[i1 / coffw,i2 / coffh],[(i1 + 1) / coffw, (i2 + 1) / coffh]],{},{fillColor: '#7df9ff33',fillOpacity: 0.5}));
        }
    }
}
