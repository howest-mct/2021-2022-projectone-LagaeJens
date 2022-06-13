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

const waardeNaarFrontendBCD = function (data) {
  let htmlstring = ''
  console.log(data.BCD)
  console.log(document.querySelector('.js-placeholderr'))
  htmlsensor = document.querySelector('.js-placeholderr').innerHTML = `<p>${data.BCD}</p>`
  // htmlstring =`<p>${data.knop}</p>`
  // htmlsensor.innerhtml = htmlstring
}





const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });

  socket.on('BCD', function (data) {
    console.log(data)
    waardeNaarFrontendBCD(data)
  });


  socket.on('knop', function (data) {
    console.log(data)
    waardeNaarFrontend(data)
  });
};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  htmlhistoriek = document.querySelector('.js-historiek')
  htmlspel = document.querySelector('.js-spel');

  listenToUI();
  listenToSocket();
  if (htmlspel) {
    listenStartbutton();
  }
  if (htmlhistoriek) {
    get_Data_historiek();
  }
});


// #region ***  DOM references                           ***********
// #endregion

// #region ***  Callback-Visualisation - show___         ***********
const show_data_historiek = function (data) {
  console.log(data)
  try {
    let html = ''
    for (let h of data.geschiedenis) {
      console.log(h)
      html += `<tr>
                        <td>${h.volgnummer}</td>
                        <td>${h.deviceid}</td>
                        <td>${h.actieid}</td>
                        <td>${h.spelerid}</td>
                        <td>${h.actiedatum}</td>
                        <td>${h.waarde}</td>
                        <td>${h.commentaar}</td>
                    </tr>`
    }
    document.querySelector('.js-tabel').innerHTML = html;
  } catch (error) {
    console.error(error);
  }

}
// #endregion

// #region ***  Callback-No Visualisation - callback___  ***********
// #endregion

// #region ***  Data Access - get___                     ***********
const get_Data_historiek = function () {
  console.log('get_Data_historiek')
  console.log(lanIP)
  handleData(`http://${lanIP}/api/v1/historiek/`, show_data_historiek);
}
// #endregion

// #region ***  Event Listeners - listenTo___            ***********
const listenToUI = function () {
  console.log('listenToUI')
};
const listenStartbutton = function () {
  console.log('listenStartbutton')
  document.querySelector('.js-startbutton').addEventListener('click', function () {
    socket.emit('f_2_b_knop');
  })
}
// #endregion

// #region ***  Init / DOMContentLoaded                  ***********

// #endregion