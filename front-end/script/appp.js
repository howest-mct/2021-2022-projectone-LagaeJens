const chart = function () {
    var stars = [135850, 52122, 148825, 16939, 9763];
    var frameworks = ['React', 'Angular', 'Vue', 'Hyperapp', 'Omi'];
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: frameworks,
            datasets: [{
                label: 'Popular JavaScript Frameworks',
                data: stars
            }]
        },
    });
}


const init = function () {
    console.log('init')
    chart();
}

document.addEventListener('DOMContentLoaded', init);