const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

let htmlsensor
let myChart
let converted_data
let id_speler
let data_player

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
  // console.log(data.BCD)
  // console.log(document.querySelector('.js-placeholderr'))
  htmlsensor = document.querySelector('.js-placeholderr').innerHTML = `<p>${data.BCD}</p>`
  // htmlstring =`<p>${data.knop}</p>`
  // htmlsensor.innerhtml = htmlstring
}




const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });

  socket.on('BCD', function (data) {
    // console.log(data)
    waardeNaarFrontendBCD(data)
  });


  socket.on('knop', function (data) {
    console.log(data)
    waardeNaarFrontend(data)
  });

  socket.on('BCD_B2F', function () {
    console.log("ok")
    window.location.href = "vragen.html"
  })

  socket.on('b2f_id', function (data) {
    id_speler = data.id
    console.log("test", id_speler)
  })

  socket.on('b2f_tijden', function (data) {
    console.log(data)
    data_player = data
    spelerchart = data
  })

};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  htmlhistoriek = document.querySelector('.js-historiek')
  htmlspel = document.querySelector('.js-spel');
  htmlvragen = document.querySelector('.js-vragen');
  htmlspelerinfo = document.querySelector('.js-spelerinfo');
  htmladmin = document.querySelector('.js-admin');
  // get_speler_data()
  listenToUI();
  listenToSocket();

  if (htmlspel) {
    listenStartbutton();
    get_top_tijden()
    listenToStartbutton2();
    test();
  }
  if (htmlhistoriek) {
    get_Data_historiek();
    waardeNaarFrontendBCD()
    waardeNaarFrontend()

  }
  if (htmlvragen) {
    Get_vragen();
  }
  if (htmlspelerinfo) {
    chart()
    show_speler_data()

  }
  if (htmladmin) {
    listenToPoweroff()
    listenToservo()
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

const shuffle = function (array) {
  for (var i = array.length - 1; i > 0; i--) {

    // Generate random number
    var j = Math.floor(Math.random() * (i + 1));

    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }

  return array;
}

const show_vragen = function (data) {
  console.log(data)
  try {
    vraagcounter = 1
    let coounter = 0
    let counter = 0
    let html = ''
    let vragen = []
    let bloknums = [3, 1, 5, 4, 6, 2]
    for (let x of data.vragen) {
      answer = `${bloknums[counter]}   |   ${x.antwoord}`
      vragen.push(answer)
      counter += 1
    }
    console.log(vragen)
    vragen_1 = shuffle(vragen)
    console.log(vragen_1)
    for (let v of data.vragen) {
      // console.log(v)
      html += `<div class="o-container js-vraag">     
             <div class="o-layout o-layout--justify-center o-layout--gutter-xl">
                <div class="card o-layout__item u-1-of-3">
                    <p>vraag ${vraagcounter}: ${v.vraag}</p>
                </div>
                <div class="card o-layout__item u-1-of-3">
                    <p>bloknr: ${vragen[coounter]}</p>
                </div>
            </div>`;
      coounter += 1
      vraagcounter += 1
    }

    document.querySelector('.js-vraag').innerHTML = html;
  } catch (error) {
    console.error(error);
  }
}

const show_top_tijden = function (data) {
  // console.log(data)
  try {
    let html = ''
    for (let t of data.top_times) {
      // console.log(t)
      html += `<tr>
                        <td>${t.spel_1}</td>
                        <td>${t.spel_2}</td>
                        <td>${t.spel_3}</td>
                        <td>${t.spel_4}</td>
                        <td>${t.totale_tijd}</td>
                    </tr>`
    }
    document.querySelector('.js-toptijden').innerHTML = html;
  } catch (error) {
    console.error(error);
  }

}

// const chart_data = function (data) {
//   // console.log(data)
//   try {
//     converted_data = [data.geschied_speler.spel_1, data.geschied_speler.spel_2, data.geschied_speler.spel_3, data.geschied_speler.spel_4]
//     console.log(converted_data);
//     dataset.data.push(converted_data)
//     myChart.update();
//   }
//   catch (error) {
//     console.error(error);
//   }
// }
let data_chart = []
let spelerchart

const show_speler_data = function () {
  const labels = ['Spel 1', 'Spel 2', 'Spel 3', 'Spel 4']
  const data = {
    labels: labels,
    datasets: [
      {
        label: 'Speler',
        data: data_chart,
        backgroundColor: "#3755ff",
        bordercolor: "#375560",
      }
    ]
  }
  const config = {
    type: 'line',
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Geschiedenis',
        }
      }
    }
  }
  const ctx = document.querySelector('.js-chart')
  spelerchart = new Chart(ctx, config)
}
const updatespelerData = function (data) {
  for (const log of data) {
    if (log['Waarde'] > 0) {
      data_chart.push(log['Waarde']);
      WeightLabels.push(log['day']);
    }
  }
  // console.log(weightData);
  weightChart.update();
};


const test = function (data) {
  let options = {
    chart: {
      type: 'bar'
    },
    series: [{
      name: 'playerdata',
      data: data_player
    }],
    xaxis: {
      categories: ['spel 1', 'spel 2', 'spel 3', 'spel 4']
    }
  }

  let chart = new ApexCharts(document.querySelector("#chart"), options);

  chart.render();
}


// const chart = function () {
//   let stars = [135850, 52122];
//   let frameworks = ['Spel 1 ', 'Spel 2', 'Spel 3', 'Spel 4'];
//   let ctx = document.getElementById('myChart');
//   myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//       labels: frameworks,
//       datasets: [{
//         label: 'Spel 1',
//         data: stars,
//         backgroundColor: [
//           "rgba(255, 99, 132, 0.2)",
//           "rgba(54, 162, 235, 0.2)",
//           "rgba(255, 206, 86, 0.2)",
//           "rgba(75, 192, 192, 0.2)",
//           "rgba(153, 102, 255, 0.2)"
//         ]
//       }]
//     },
//   });

// }
// #endregion

// #region ***  Callback-No Visualisation - callback___  ***********


// #endregion

// #region ***  Data Access - get___                     ***********
function get_Data_historiek() {
  console.log('get_Data_historiek');
  console.log(lanIP);
  handleData(`http://${lanIP}/api/v1/historiek/`, show_data_historiek);
}
const Get_vragen = function () {
  console.log('vragen opgehaald')
  handleData(`http://${lanIP}/api/v1/vragen/`, show_vragen);

}

const get_top_tijden = function () {
  console.log('get_top_tijden')
  handleData(`http://${lanIP}/api/v1/spelerinlog/`, show_top_tijden);
}

const get_top_tijden2 = function () {
  console.log('get_top_tijden')
  handleData(`http://${lanIP}/api/v1/spelerinlog/`, test);
}

const get_speler_data = function () {
  console.log('get_speler_data')
  handleData(`http://${lanIP}/api/v1/spelersinfo/137/`, show_speler_data);
}




// #endregion

// #region ***  Event Listeners - listenTo___            ***********
function listenToUI() {
  console.log('listenToUI');
}
const listenStartbutton = function () {
  console.log('listenStartbutton')
  document.querySelector('.js-startbutton').addEventListener('click', function () {
    socket.emit('f_2_b_knop')
  });
}

const listenToservo = function () {
  console.log('listenToservo')
  document.querySelector('.js-servo').addEventListener('click', function () {
    socket.emit('f_2_b_servo')
  })
}

const listenToPoweroff = function () {
  console.log('listenToPoweroff')
  document.querySelector('.js-poweroff').addEventListener('click', function () {
    socket.emit('f_2_b_poweroff')
  })
}

const show_insert_klaar = function (jsonObject) {
  console.log('ok')
}

const listenToStartbutton2 = function () {
  console.log('listenToStartbutton2')
  try {
    document.querySelector('.js-startbutton').addEventListener('click', function () {
      const jsonObject = JSON.stringify({
        naam: document.querySelector('.js-naam').value,
        kaartnummer: parseInt(document.querySelector('.js-kaart').value)
      })
      console.log(jsonObject)
      handleData(`http://${lanIP}/api/v1/spelerinlog/`, show_insert_klaar, null, 'POST', jsonObject);
    })
  } catch (error) {
    console.error(error);
  }
}



// #endregion


// #region ***  Init / DOMContentLoaded                  ***********


// #endregion