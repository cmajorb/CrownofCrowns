function findPos(obj) {
    var curleft = 0, curtop = 0;
    if (obj.offsetParent) {
        do {
            curleft += obj.offsetLeft;
            curtop += obj.offsetTop;
        } while (obj = obj.offsetParent);
        return { x: curleft, y: curtop };
    }
    return undefined;
}

function rgbToHex(r, g, b) {
    if (r > 255 || g > 255 || b > 255)
        throw "Invalid color component";
    return ((r << 16) | (g << 8) | b).toString(16);
}


window.onload = function() {
    var map = document.getElementById("map");
    var ctx = map.getContext("2d");
    var img = new Image();

    img.src = "images/map.png";
   ctx.drawImage(img, 0, 0,1200,800);

   var colorgrid = document.getElementById("colorgrid");
   var ctx2 = colorgrid.getContext("2d");
   var img2 = new Image();

   img2.src = "images/colormap.png";
  ctx2.drawImage(img2, 0, 0,1200,800);
};

$('#colorgrid').mousemove(function(e) {
    var name;
    var pos = findPos(this);
    var x = e.pageX - pos.x;
    var y = e.pageY - pos.y;
    var coord = "x=" + x + ", y=" + y;
    var c = this.getContext('2d');
    var p = c.getImageData(x, y, 1, 1).data;
    var hex = "#" + ("000000" + rgbToHex(p[0], p[1], p[2])).slice(-6);
    for(var i = 0; i<loc.length;i++) {
      if(loc[i].Color==hex) {
        name = loc[i].Location;
      }
    }
    $('#status').html(coord + "<br>" + name + "<br>"+hex);
});
var loc;
$('#colorgrid').click(function(e) {
    var pos = findPos(this);
    var x = e.pageX - pos.x;
    var y = e.pageY - pos.y;
    var c = this.getContext('2d');
    var p = c.getImageData(x, y, 1, 1).data;
    var hex = "#" + ("000000" + rgbToHex(p[0], p[1], p[2])).slice(-6);
    alert(hex);
});

$(document).ready(function(){
  $.getJSON('http://localhost:9000/get_map_locations', function(data) {
    var i;
    loc = data;
    for(i = 0; i<data.length; i++) {
      $("#itemTable").append("<tr><td>"+data[i][0]+"</td><td>"+data[i][1]+"</td></tr>");
    }
  });
  $("#itemInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#itemTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
