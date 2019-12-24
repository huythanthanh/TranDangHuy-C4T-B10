var el = document.getElementById("song_container");
el.addEventListener('click', function(g) {
    var element = g.target;
    var eldiv = element.parentNode;
    console.log(eldiv);
})


var delbutton = document.getElementsByClassName("del_button");

for ( var i = 0; i < delbutton.length; i++) {
    var delbutton2 = delbutton [i];
    delbutton2.addEventListener('click', function(e) {
        var del = e.target;
        var div = del.parentNode;
        div.remove();
    });
}

var editbutton = document.getElementsByClassName('edit_button');

for (var a = 0; a < editbutton.length; a++) {
    var editbutton2 = editbutton [a];
    editbutton2.addEventListener('click', function(f) {
        var edit = f.target;
        console.log(f.path[1].attributes[1].value)
    });
}

var morebutton = document.getElementsByClassName('more_button');
for (var m = 0; m < morebutton.length; m++) {
    var morebutton2 = morebutton [m];
    morebutton2.addEventListener('click', function(k) {
        var more = k.target;
        console.log(k.path[1].attributes[1].value);
        console.log(k.path[1].attributes[2].value);
        console.log(k.path[1].attributes[3].value)
    })
}

var addbutton = document.getElementsByClassName('add_button');
for (var o = 0; o < addbutton.length; o++) {
    addbutton [o].addEventListener('click', function(q) {
        var SongContainer = document.getElementById("song_container");
        var newHTML = `<div class="song" song_id="78ab12" song="Girls like you" artist="Maroon 5">
        <h4 class="title">Girls like you</h4>
        <h5 class="artist">Maroon 5</h5>
        <button class="del_button">Delete</button>
        <button class="edit_button">Edit</button>
        <button class="more_button">More</button>
        <button class="add_button">Add</button>
      </div>`
      SongContainer.insertAdjacentHTML("beforeend", newHTML)
    });
}