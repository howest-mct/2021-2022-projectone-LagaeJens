import ApexCharts from 'apexcharts'
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
  htmlvragen = document.querySelector('.js-vragen');

  listenToUI();
  listenToSocket();
  if (htmlspel) {
    listenStartbutton();
  }
  if (htmlhistoriek) {
    myChart()
    get_Data_historiek();
  }
  if (htmlvragen) {
    Get_vragen();
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

const show_vragen = function (data) {
  console.log(data)
  try {
    let html = ''
    for (let v of data.vragen) {
      // console.log(v)
      html = `<div class="o-container js-vraag">     
             <div class="o-layout o-layout--justify-center o-layout--gutter-xl">
                <div class="card o-layout__item u-1-of-2">
                    <p>vraag 1: ${v.vraag}</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>${v.antwoord}</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>vraag 2: ${v.vraag}</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>antwoord</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>vraag 3: ${v.vraag}</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>antwoord</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>vraag 4: ${v.vraag}</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>antwoord</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>vraag 5: ${v.vraag}</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>antwoord</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>vraag 6: ${v.vraag}</p>
                </div>
                <div class="card o-layout__item u-1-of-2">
                    <p>antwoord</p>
                </div>
            </div>
            </div>`}
    document.querySelector('.js-vraag').innerHTML = html;
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
const Get_vragen = function () {
  console.log('vragen opgehaald')
  handleData(`http://${lanIP}/api/v1/vragen/`, show_vragen);
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
var options = {
  chart: {
    type: 'line'
  },
  series: [{
    name: 'sales',
    data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
  }],
  xaxis: {
    categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
  }
}

var chart = new ApexCharts(document.querySelector('#js-chart'), options);

chart.render()

// #region ***  Init / DOMContentLoaded                  ***********


// #endregion