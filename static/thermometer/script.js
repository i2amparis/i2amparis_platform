
const units = {
  Celcius: "°C",
  Fahrenheit: "°F" };


const config = {
  minTemp: min_temp,
  maxTemp: max_temp,
  unit: "Celcius" };


// Change min and max temperature values

const tempValueInputs = document.querySelectorAll("input[type='text']");

//tempValueInputs.forEach(input => {
//  input.addEventListener("change", event => {
//    const newValue = event.target.value;
//
//    if (isNaN(newValue)) {
//      return input.value = config[input.id];
//    } else {
//      config[input.id] = input.value;
//      range[input.id.slice(0, 3)] = config[input.id]; // Update range
//      return setTemperature(); // Update temperature
//    }
//  });
//});

// Switch unit of temperature

// const unitP = document.getElementById("unit");
//
// unitP.addEventListener("click", () => {
//   config.unit = config.unit === "Celcius" ? "Fahrenheit" : "Celcius";
//   unitP.innerHTML = config.unit + ' ' + units[config.unit];
//   return setTemperature();
// });

// Change temperature

var range = document.querySelector("input[type='range']");
var temperature = document.getElementById("temperature");

function setTemperature() {
  temperature.style.height = (range.value - config.minTemp) / (config.maxTemp - config.minTemp) * 100 + "%";
  temperature.dataset.value = range.value + units[config.unit];
}

$(document).ready(function () {
  // setTemperature();
});



// function lineChart(t) {
var t= 1;
  am4core.ready(function() {

// Themes begin
    am4core.useTheme(am4themes_animated);
// Themes end

// Create chart instance
    var chart = am4core.create("chartdiv", am4charts.XYChart);

// Add data
//    chart.data = myData(1);

    chart.data = [];

// Set input format for the dates
    chart.dateFormatter.inputDateFormat = "yyyy-MM-dd";

// Create axes
    var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.renderer.minGridDistance = 50;
    dateAxis.title.fontWeight = 600;
    dateAxis.title.marginTop = 10;
    dateAxis.title.marginBottom = 20;
    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.title.fontWeight = 600;

// Create series
    var series = chart.series.push(new am4charts.LineSeries());
    series.dataFields.valueY = "value";
    series.dataFields.dateX = "date";
    series.strokeWidth = 2;
    series.minBulletDistance = 10;
    series.tooltipText = "{valueY.value}";
    series.tooltip.pointerOrientation = "vertical";
    series.tooltip.background.cornerRadius = 20;
    series.tooltip.background.fillOpacity = 0.8;
    series.tooltip.label.padding(12, 12, 12, 12);
    series.tooltip.autoTextColor = false;
    series.tooltip.label.fill = am4core.color("#FFFFFF");
    series.tooltip.getFillFromObject = false;
    series.tooltip.background.fill = am4core.color("#63A1DB").lighten(-0.3);

    series.legendSettings.labelText = "{name}";
    series.legendSettings.itemValueText = "[bold]{valueY}[/bold]";
    series.fill = am4core.color("#63A1DB");
    series.stroke = am4core.color("#63A1DB");
    //Smoothed Lines
    series.tensionX = 0.9;
    series.fillOpacity = 1;
    let fillModifier = new am4core.LinearGradientModifier();
    fillModifier.opacities = [0.3, 0];
    fillModifier.offsets = [0, 0.5];
    fillModifier.gradient.rotation = 90;
    series.segments.template.fillModifier = fillModifier;

    //Add Legend
    chart.legend = new am4charts.Legend();
    chart.legend.useDefaultMarker = true;
    var marker = chart.legend.markers.template.children.getIndex(0);
    marker.cornerRadius(5, 5, 5, 5);
    marker.strokeWidth = 2;
    marker.strokeOpacity = 1;
    marker.stroke = am4core.color("#ccc");
    var markerTemplate = chart.legend.markers.template;
    markerTemplate.width = 25;
    markerTemplate.height = 25;

// Drop-shaped tooltips
    series.tooltip.background.cornerRadius = 20;
    series.tooltip.background.strokeOpacity = 0;
    series.tooltip.pointerOrientation = "vertical";
    series.tooltip.label.minWidth = 40;
    series.tooltip.label.minHeight = 40;
    series.tooltip.label.textAlign = "middle";
    series.tooltip.label.textValign = "middle";


// Make a panning cursor
    chart.cursor = new am4charts.XYCursor();
    chart.cursor.xAxis = dateAxis;

    // Add scrollbar
    chart.scrollbarX = new am4charts.XYChartScrollbar();
    chart.scrollbarX.series.push(series);


    dateAxis.keepSelection = true;




// }
// Function which call at the begin to set start temperature
function setStartTemp(temp) {
document.getElementById("input_temp").value = temp;
temperature.style.height = (temp - config.minTemp) / (config.maxTemp - config.minTemp) * 100 + "%";
 temperature.dataset.value = temp + units[config.unit];
 chart.data= recordDataFun(temp);
 }

 function setTemp(){
 var temp = document.getElementById("input_temp").value;
 setStartTemp(temp);
 }
// Get the first key of the recordData hash map
temp = Object.keys(recordData)[0];
setStartTemp(temp);
document.getElementById("termometer").addEventListener("wheel", myFunction);
document.getElementById("input_temp").addEventListener("change", setTemp);

var temp = 0;

function myFunction(e) {
  if (e.deltaY < 0) {
    if (config.maxTemp > temp) {
      temp += 1;}
  } else {
    if (config.minTemp < temp) {
      temp -= 1;
    }

  }

// Set temperature in input text
document.getElementById("input_temp").value = temp;
//  chart.data= myData(temp);

  chart.data= recordDataFun(temp);
  temperature.style.height = (temp - config.minTemp) / (config.maxTemp - config.minTemp) * 100 + "%";
  console.log(temperature.style.height);
  temperature.dataset.value = temp + units[config.unit];
}
// var flag= true;
// if (flag) {
//   lineChart(1);
//   flag = false;
// }
  }); // end am4core.ready()
function myData(t) {
  tempInputData = inputData;
  for (let i = 0; i < tempInputData.length; i++){
            tempInputData[i].value = tempInputData[i].value *t;
            }
  return tempInputData;

}


function recordDataFun(key){
// In case we have records
if (recordData[key]=== undefined){
    // If there isn't this key return empty array
    return [];
}else{
        return recordData[key];
}
}