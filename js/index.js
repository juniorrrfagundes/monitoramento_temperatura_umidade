

let temp = [];
let umid = [];
let data_pesquisa = [];

async function pegar_json(){
    let response = await fetch("http://127.0.0.1:5000/sensor");
    let json = await response.json();
    let obj = json['Dados']
    for (let i=0; i < obj.length; i++){
        temp.push(obj[i]['temperatura']);
        umid.push(obj[i]['umidade']);
        data_pesquisa.push(obj[i]['data']);
    };
};

pegar_json();


function grafico(ctx){

    let labels = data_pesquisa
    let datasets = [
        {
            label: 'Temperatura',
            data: temp,
            fill: false,
            borderColor: 'rgb(75, 192, 0)',
            tension: 0.1
          },
          {
            label: 'Umidade',
            data: umid,
            fill: false,
            borderColor: 'rgb(0, 192, 192)',
            tension: 0.1
          }
    ]

    let data = {
        labels: labels,
        datasets: datasets
      };
    
      return new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      })

};

let ctx = document.getElementById("mychart");
let chart = grafico(ctx)

