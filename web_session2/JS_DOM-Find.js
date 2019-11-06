var el = document.getElementById("song_container");
console.log(el)

var delbutton = document.getElementsByClassName("del_button");

for ( var i = 0; i < delbutton.length; i++) {
    var delbutton2 = delbutton [i];
    delbutton2.addEventListener('click', function(e) {
        var del = e.target;
        var div = del.parentNode;
        div.remove();
    });
}

