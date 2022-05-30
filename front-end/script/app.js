const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);




const listenToUI = function () {  
};

const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });

  socket.on('knop',function(data){
    console.log(data)
  });
};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  listenToUI();
  listenToSocket();
});
