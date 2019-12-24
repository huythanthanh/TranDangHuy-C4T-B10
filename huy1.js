
var myJsons = document.getElementById('card');
for (var o = 0; o < myJsons.length; o++) {
    var Container = document.getElementById("card");
    var ${newHTML} = `async function takeData() {
            const response = await fetch('http://5dde608afca1110014f1634d.mockapi.io/firstAPI');
            const myJson = await response.json();`
    Container.insertAdjacentHTML("beforeend", newHTML)

}


takeData()

