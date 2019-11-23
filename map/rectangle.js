function init () {
    var cofflon = 200, startlon = 11114, stoplon = 11180;
    var cofflat = 100, startlat = 3737, stoplat = 3783;
    var myMap = new ymaps.Map('map',{center: [55.753960, 37.620393],zoom: 12});
    for(var counterlon = startlon; counterlon <= stoplon; counterlon++){
        for(var counterlat = startlat; counterlat <= stoplat; counterlat++){
            myMap.geoObjects.add(new ymaps.Rectangle([[counterlon / cofflon,stoplat / cofflat],[(counterlon + 1) / cofflon, (stoplat + 1) / cofflat]],{},{fillColor: '#7df9ff33',fillOpacity: 0.5}));
        }
    }
};

ymaps.ready(init);