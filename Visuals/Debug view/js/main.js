//prevent rest of js from running until page is loaded

$(document).ready(function () {
    console.log("Page has loaded");
    
    setTimeout(function () {
        init();
    }, 1000);
});

//initialization function
function init() {
    console.log("init() called");
    setSpeedLimit(34);
    setCurrentSpeed(34);
    plotSpeed();
    setInterval(function () {
        increaseSpeed();
        updatePlot();
        setTime();
    }, 3000);
}

//miscellaneous functions
function getSystemTime() {
    /* slice date function to get current time */
    var date = new Date();
    var time = date.toTimeString();
    var time = time.slice(0, 8);
    return time;
}
function setTime() {
    var time = getSystemTime();
    var timeElement = document.getElementById("system_time");
    var hours = time.slice(0, 2);
    var minutes = time.slice(3, 5);
    var seconds = time.slice(6, 8);
    if (hours > 12) {
        hours = hours - 12;
        time = hours + ":" + minutes + ":" + seconds + " PM";
    }
    else {
        time = hours + ":" + minutes + ":" + seconds + " AM";
    }
    timeElement.innerHTML = time;
}


//manipulate current speed & speed limit
function getSpeedLimit() {
    var speedLimit = document.getElementById("current_speed_limit");
    return speedLimit.innerHTML;
}
function setSpeedLimit(speed) {
    var speedLimit = document.getElementById("current_speed_limit");
    speedLimit.innerHTML = speed;
}
function getCurrentSpeed() {
    var currentSpeed = document.getElementById("current_speed");
    return currentSpeed.innerHTML;
}
function setCurrentSpeed(speed) {
    var currentSpeed = document.getElementById("current_speed");
    currentSpeed.innerHTML = speed;
}
function increaseSpeed() {
    var speedLimit = getSpeedLimit();
    var currentSpeed = getCurrentSpeed();
    currentSpeed++;
    setCurrentSpeed(currentSpeed);
    console.log("Speed limit is " + speedLimit);
    console.log("Current speed is " + currentSpeed);
}
function decreaseSpeed() {
    var speedLimit = getSpeedLimit();
    var currentSpeed = getCurrentSpeed();
    currentSpeed--;
    setCurrentSpeed(currentSpeed);
    console.log("Speed limit is " + speedLimit);
    console.log("Current speed is " + currentSpeed);
}

//plotly functions for speed limit vs current speed
function plotSpeed() {
    var speedLimit = getSpeedLimit();
    var currentSpeed = getCurrentSpeed();
    var data = [{
        x: [getSystemTime()],
        y: [speedLimit],
        type: 'scatter'
    },
    {
        x: [getSystemTime()],
        y: [currentSpeed],
        type: 'scatter'
    }];
    var layout = {
        title: 'Speed Limit vs Current Speed',
        xaxis: {
            title: 'Time'
        },
        yaxis: {
            title: 'Speed (km/h)'
        }
    };
    Plotly.newPlot('speed_plot', data, layout);
}
function updatePlot() {
    var speedLimit = getSpeedLimit();
    var currentSpeed = getCurrentSpeed();
    var update = {
        x: [[getSystemTime()], [getSystemTime()]],
        y: [[speedLimit], [currentSpeed]]
    };
    Plotly.extendTraces('speed_plot', update, [0, 1]);
}


