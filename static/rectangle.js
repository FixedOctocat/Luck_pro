function div(val, by){
    return (val - val % by) / by;
}

function init(egor_square){
    return function(){
        myMap = new ymaps.Map('map',{center: [55.753960, 37.620393],zoom: 12.5,controls:['zoomControl']});
        myMap.geoObjects.add(new ymaps.Rectangle([[1,1],[2,2]],{},{}))
        myColl = new ymaps.GeoObjectCollection();
        districs = [], part = [];
        for(var counterlon = 0; counterlon < egor_square.length; counterlon++){
            part = [];
            for(var counterlat = 0; counterlat < egor_square[counterlon].length; counterlat++){
                if (egor_square[counterlon][counterlat][2] >= 0){
                    red = 0;
                    green = 100 + Math.ceil(155 * egor_square[counterlon][counterlat][2]);
                } else {
                    green = 0;
                    red = 100 + Math.ceil(155 * -egor_square[counterlon][counterlat][2]);
                };
                color = 'rgb(' + red.toString() + ',' + green.toString() + ',0)';
                coords = egor_square[counterlon][counterlat]
                newSquare = new ymaps.Rectangle(coords.slice(0,2),{},{fillColor: color,fillOpacity: 0.5})
                part.push(newSquare);
            }
            districs.push(part);
        }
    }
};

// godef = [[[[55.57, 37.37], [55.575, 37.38], 0.7777253209378436], [[55.57, 37.38], [55.575, 37.39], 0.5891686084953953]]];

function fillSquare(ids){
    return function(){
        myColl.removeAll();
        myMap.geoObjects.remove(0);
        for(var counter = 0;counter < ids.length; counter++){
            var gor = 46, gorid = ids[counter] % gor, verid = div(ids[counter],gor);
            myColl.add(districs[verid][gorid]);
        }
        myMap.geoObjects.add(myColl);
        myMap.setBounds(myColl.getBounds());
    }
}


// ymaps.ready(init(godef));
// ymaps.ready(fillSquare([0,1])); 