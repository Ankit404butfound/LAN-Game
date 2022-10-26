var ball = document.getElementById("ball");
var dx = 3;
var dy = 0;
var count = 0;

var height = window.innerHeight - (0.06 * window.innerHeight) + 5;
var width = screen.width;


function draw() {
    var left = window.getComputedStyle(ball).getPropertyValue("left").replace("px","");
    var bottom = window.getComputedStyle(ball).getPropertyValue("bottom").replace("px","")
    
    if (left > width-50 || left < 10) {
        dx = -dx;
    }
    if (bottom > height-50 || bottom < 10) {
        dy = -dy;
    }

    ball.style.left = (Number(left)+dx)+"px";
    ball.style.bottom = (Number(bottom)+dy)+"px";
    requestAnimationFrame(draw)
}

function countDown() {
    count++;
    console.log(count);
}
// setInterval(draw, 10);
setInterval(countDown, 1000);
requestAnimationFrame(draw);