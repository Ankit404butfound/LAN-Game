#render index.html
from flask import Flask
import json

app = Flask(__name__)

playersData = {"coords": [1]}

@app.route('/')

def index():
    return """<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>Gamedev Canvas Workshop</title>
    <style>
      .ball {
            left: 1%;
            background-color: rgb(253, 139, 0);
            bottom: 60%;
            width:50px;
            height: 50px;
            position: absolute;
            border-radius: 50%
        }
    </style>
  </head>
  <body>
    <div class=ball id="ball"></div>
  </body>
  <script>
    var ball = document.getElementById("ball");
var dx = 3;
var dy = 0;
var count = 0;
var xhttp = new XMLHttpRequest();

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
    xhttp.onload = function() {
        var j = Number(this.responseText);
        console.log(j);
        if (j == 0) {
            dx = -1
            dy = -2
            }
        }
    xhttp.open("GET", "getCoords", true);
    xhttp.send();
}
// setInterval(draw, 10);
setInterval(countDown, 10);
requestAnimationFrame(draw);
  </script>
</html>"""

@app.route("/update/<x>")
def updateCoords(x):
    playersData["coords"] = [x]
    return "OK"

@app.route("/getCoords")
def getCoords():
    return str(playersData["coords"][0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
