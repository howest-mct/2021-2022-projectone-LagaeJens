const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

let htmlsensor

const waardeNaarFrontend = function (data) {
let htmlstring = ''
console.log(data.knop)
console.log(document.querySelector('.js-placeholder'))
htmlsensor = document.querySelector('.js-placeholder').innerHTML = `<p>${data.knop}</p>` 
// htmlstring =`<p>${data.knop}</p>`
// htmlsensor.innerhtml = htmlstring
}


const listenToUI = function () {  
};

const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });
  
  socket.on('knop',function(data){
    console.log(data)
    waardeNaarFrontend(data)
  });
};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  listenToUI();
  listenToSocket();
});
