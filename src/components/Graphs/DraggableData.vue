<template>
    <Line data={data} options={options} />
</template>

<script setup>
import { Line } from "vue-chartjs";
import "chartjs-plugin-dragdata";

const options = {
  tooltips: { enabled: true },
  scales: {
    xAxes: [
      {
        gridLines: { display: false, color: "grey" },
        ticks: { fontColor: "#3C3C3C", fontSize: 14 }
      }
    ],
    yAxes: [
      {
        scaleLabel: {
          display: true,
          labelString: "Color Strength",
          fontSize: 14
        },
        ticks: {
          display: true,
          min: -5,
          max: 100,
          scaleSteps: 50,
          scaleStartValue: -50,
          maxTicksLimit: 4,
          fontColor: "#9B9B9B",
          padding: 30,
          callback: point => (point < 0 ? "" : point)
        },
        gridLines: {
          display: false,
          offsetGridLines: true,
          color: "3C3C3C",
          tickMarkLength: 4
        }
      }
    ]
  },
  legend: {
    display: true
  },
  dragData: true,
  onDragStart: function(e) {
    console.log(e);
  },
  onDrag: function(e, datasetIndex, index, value) {
    console.log(datasetIndex, index, value);
  },
  onDragEnd: function(e, datasetIndex, index, value) {
    console.log(datasetIndex, index, value);
  }
};

}

</script>
