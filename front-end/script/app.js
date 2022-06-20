const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

let htmlsensor
let htmlsensors
let myChart
let converted_data
let id_speler
let data_player

const waardeNaarFrontend = function (data) {
  let htmlstrings = ''
  // console.log(data.b2f_mpu)
  console.log(document.querySelector('.js-BCD'))
  htmlsensors = document.querySelector('.js-BCD').innerHTML = `<p>BCD waarde: ${data.BCD}</p>`
  // htmlstrings = `<p>Waarde MPU: ${data.b2f_mpu}</p>`
  // htmlsensors.innerhtml = htmlstrings
}

const waardeNaarFrontendMPU = function (data) {
  let htmlstring = ''
  // console.log(data.BCD)
  console.log(document.querySelector('.js-mup'))
  htmlsensor = document.querySelector('.js-mup').innerHTML = `<p>MPU waarde: ${data.b2f_mpu}</p>`
  // htmlstring = `<p>BCD waarde: ${data.knop}</p>`
  // htmlsensor.innerhtml = htmlstring
}




const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });

  socket.on('b2f_mpu', function (data) {
    // console.log(data)
    waardeNaarFrontendMPU(data)
  });


  socket.on('BCD', function (data) {
    console.log(data)
    waardeNaarFrontend(data)
  });

  socket.on('BCD_B2F', function () {
    console.log("ok")
    window.location.href = "vragen.html"
  })

  socket.on('b2f_id', function (data) {
    id_speler = data.id
    localStorage.setItem('id_speler', id_speler);
    console.log("test", id_speler)
  })

  socket.on('b2f_tijden', function (data) {
    console.log(data)
    data_player = data
    spelerchart = data
  })
  socket.on('b2f_einde', function () {
    console.log("einde")
    window.location.href = "spelersinfo.html"
  })
  socket.on('gestart', function () {
    console.log("gestart")
  })
  socket.on('gestart2', function () {
    console.log("gestart2")
  })
  socket.on('gestart3', function () {
    console.log("gestart3")
  })
};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  htmlhistoriek = document.querySelector('.js-historiek')
  htmlspel = document.querySelector('.js-spel');
  htmlvragen = document.querySelector('.js-vragen');
  htmlspelerinfo = document.querySelector('.js-spelerinfo');
  htmladmin = document.querySelector('.js-admin');
  htmlsensorinfo = document.querySelector('.js-sensorinfo');


  // get_speler_data()
  listenToUI();
  listenToSocket();
  toggleNav()
  if (htmlspel) {
    listenStartbutton();
    get_top_tijden()
    listenToStartbutton2();
    test();
  }
  if (htmlhistoriek) {
    get_history_spelers()
  }
  if (htmlvragen) {
    Get_vragen();
  }
  if (htmlsensorinfo) {
    get_Data_historiek();
    waardeNaarFrontendMPU()
    waardeNaarFrontend()
  }


  if (htmlspelerinfo) {
    // show_speler_data()
    const id_spelr = localStorage.getItem('id_speler')
    console.log(id_spelr, "lolololo")
    get_speler_data(id_spelr)

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
  console.log(id_speler)
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
             <div class="o-layout o-layout--justify-center">
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
  try {
    let html = ''
    for (let t of data.top_times) {
      // console.log(t)
      html += `<tr>
                        <td>${t.naam}</td>
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

const show_spelers_tijden = function (data) {
  console.log(data)
  try {
    let html = ''
    for (let t of data.historiek) {
      console.log(t)
      html += `<tr>
                        <td>${t.naam}</td>
                        <td>${t.spel_1}</td>
                        <td>${t.spel_2}</td>
                        <td>${t.spel_3}</td>
                        <td>${t.spel_4}</td>
                        <td>${t.totale_tijd}</td>
                    </tr>`
    }
    document.querySelector('.js-tijden_spelers').innerHTML = html;
  } catch (error) {
    console.error(error);
  }
}



const show_speler_data = function (data) {
  console.log(data)
  console.log(id_speler)
  try {
    let html = ''
    {
      // console.log(i)
      html = `<tr>
                        <td>${data.geschied_speler.spel_1}</td>
                        <td>${data.geschied_speler.spel_2}</td>
                        <td>${data.geschied_speler.spel_3}</td>
                        <td>${data.geschied_speler.spel_4}</td>
                        <td>${data.geschied_speler.totale_tijd}</td>
                    </tr>`
    }
    document.querySelector('.js-spelerinfotabel').innerHTML = html;
  } catch (error) {
    console.error(error);
  }

}


const toggleNav = function () {
  let toggleTrigger = document.querySelectorAll('.js-toggle-nav');
  for (let i = 0; i < toggleTrigger.length; i++) {
    toggleTrigger[i].addEventListener('click', function () {
      document.querySelector('body').classList.toggle('has-mobile-nav');
    });
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

const get_history_spelers = function () {
  console.log('get_history_spelers')
  handleData(`http://${lanIP}/api/v1/spelerhistory/`, show_spelers_tijden);
}


const get_speler_data = function (id_speler) {
  console.log('get_speler_data', id_speler)
  try {
    handleData(`http://${lanIP}/api/v1/spelersinfo/${id_speler}/`, show_speler_data);
  } catch (error) {
    console.error(error);
  }
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