const lanIP = `${window.location.hostname}: 5000`; //!!! PAS DIT AAN ZODAT DIT dynamisch wordt !!!
// !!
const socketio = io(lanIP);

let CoffeeData = [];
let weightData = [];
let WeightLabels = [];
let CoffeeLabels = [];
let CoffeeChart;
let weightChart;

const createWeightChart = function () {
    const labels = WeightLabels;
    const data = {
        labels: labels,
        datasets: [
            {
                label: 'Weight in grams',
                data: weightData,
                backgroundColor: '#357560',
                borderColor: '#357560',
            },
        ],
    };

    const config = {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Weight of coffee pot this week',
                },
            },
        },
    };

    const ctx = document.querySelector('.coffee-weight');
    weightChart = new Chart(ctx, config);
};



const show_speler_data = function (data) {
    for (const log of data.geschied_speler) {
        CoffeeData.push(log['spel_1']);
        CoffeeData.push(log['spel_2']);
        CoffeeData.push(log['spel_3']);
        CoffeeData.push(log['spel_4']);
    }
    // console.log(CoffeeData);
    CoffeeChart.update();
};
// const  = function (data) {
//     for (const log of data) {
//         if (log['Waarde'] > 0) {
//             weightData.push(log['Waarde']);
//             WeightLabels.push(log['day']);
//         }
//     }
//     // console.log(weightData);
//     weightChart.update();
// };

socketio.on('B2F_coffeeLogs', function (data) {
    updateCoffeMade(data.coffee_logs);
});
socketio.on('B2F_weightLogs', function (data) {
    updateWeightData(data.weight_logs);
});

//#region ***  Init / DOMContentLoaded                  ***********
const init = function () {
    createCoffeeMadeChart();
    createWeightChart();
    getData();
    listenToMobileNav();
    listenToBtn();
    get_speler_data2()
};

const get_speler_data2 = function () {
    console.log('get_speler_data')
    handleData(`http://${lanIP}/api/v1/spelersinfo/137/`, show_speler_data);
}

document.addEventListener('DOMContentLoaded', init);
//#endregion