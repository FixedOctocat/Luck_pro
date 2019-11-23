function init () {
    var districs = [], part = [];
    var cofflon = 200, startlon = 11114, stoplon = 11180;
    var cofflat = 100, startlat = 3737, stoplat = 3783;
    var myMap = new ymaps.Map('map',{center: [55.753960, 37.620393],zoom: 12,controls:['zoomControl']});
    for(var counterlon = startlon; counterlon <= stoplon; counterlon++){
        part = [];
        for(var counterlat = startlat; counterlat <= stoplat; counterlat++){
            newSquare = new ymaps.Rectangle([[counterlon / cofflon,counterlat / cofflat],[(counterlon + 1) / cofflon, (counterlat + 1) / cofflat]],{},{fillColor: '#7df9ff33',fillOpacity: 0.5});
            myMap.geoObjects.add(newSquare);
        }
        districs.push[part];
    }
};

function fillSquare(ids){
    var counter = 0;
    for(;counter < ids.lenght(); counter++){
        
    }
}

ymaps.ready(init);