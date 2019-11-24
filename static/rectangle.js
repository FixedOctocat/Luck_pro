function div(val, by){
    return (val - val % by) / by;
}

function init(egor_square){
    return function(){
        myMap = new ymaps.Map('map',{center: [55.753960, 37.620393],zoom: 12.5,controls:['zoomControl']});
        districs = [], part = [];
        for(var counterlon = 0; counterlon < egor_square.length; counterlon++){
            part = [];
            for(var counterlat = 0; counterlat < egor_square[counterlon].length; counterlat++){
                if (egor_square[counterlon][counterlat][2] >= 0){
                    red = 0;
                    green = Math.ceil(255 * egor_square[counterlon][counterlat][2]);
                } else {
                    green = 0;
                    red = Math.ceil(255 * -egor_square[counterlon][counterlat][2]);
                };
                color = 'rgb(' + red.toString() + ',' + green.toString() + ',0)';
                coords = egor_square[counterlon][counterlat]
                newSquare = new ymaps.Rectangle(coords.slice(0,2),{},{fillColor: color,fillOpacity: 0.5})
                console.log(newSquare)
                part.push(newSquare);
            }
            districs.push(part);
        }
    }
};
godef = [[[[55.57, 37.37], [55.575, 37.38], 0.7777253209378436], [[55.57, 37.38], [55.575, 37.39], 0.5891686084953953]]];

ymaps.ready(init(godef));

function fillSquare(ids){
    return function(){
        for(var counter = 0;counter < ids.length; counter++){
            var gor = 46, gorid = ids[counter] % gor, verid = div(ids[counter],gor);
            console.log(verid,gorid,districs[verid][gorid])
            myMap.geoObjects.add(districs[verid][gorid]);
        }
        console.log(1111111111111)
    }
    
}

ymaps.ready(fillSquare([0,1]));