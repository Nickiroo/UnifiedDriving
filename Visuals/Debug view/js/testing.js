function randomSpeed() {
    /* Have the speed fluctuate up and down by 1 km/h at a time randomly every 5 seconds but if the speed drops below 25 then make sure it goes back up to 34 before being random again*/
    var speedLimit = getSpeedLimit();
    var randomSpeed = Math.floor(Math.random() * 3) + 1;
    var randomDirection = Math.floor(Math.random() * 2) + 1;
    if (randomDirection == 1) {
        speedLimit = parseInt(speedLimit) + parseInt(randomSpeed);
    }
    else {
        speedLimit = parseInt(speedLimit) - parseInt(randomSpeed);
    }
    if (speedLimit < 25) {
        speedLimit = 34;
    }
    setSpeedLimit(speedLimit);
    console.log("Speed limit is now " + speedLimit + " km/h");
    console.log("Speed limit changed by " + randomSpeed + " km/h");

}