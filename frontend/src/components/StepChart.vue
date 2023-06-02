<template>
    <Line :data="dp" :options="options" />
</template>
  
<script lang="ts">
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'
  
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)
  
  export default {
    name: 'App',
    props: ['datapoints'],
    components: {
      Line
    },
    data() {
        return {
            options: {
                responsive: true,
                interaction: {
                    mode: 'index'
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Rates of indicators by time',
                    }
                },
                scales: {
                    y: {
                        // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                        min: -0.1,

                        // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                        max: 1.1,
                    }
                }
            }
        }
    },
    computed: {
      dp() {
        return {
          labels: ["9:30", "10:00", "10:30", "11:00",
          "11:30", "12:00", "12:30", "13:00", "13:30",
          "14:00", "14:30", "15:00", "15:30", "16:00",
          "16:30", "17:00", "17:30", "18:00"],
          datasets: [
            {
                label: "PPE rate",
                data: this.datapoints.ppe,
                backgroundColor: 'rgba(252, 3, 3, 0.3)',
                borderColor: 'rgba(252, 3, 3, 0.3)',
                fill: false,
                stepped: true,
                pointRadius: 3,
                pointStyle: 'circle'
            },
            {
                label: "danger rate",
                data: this.datapoints.danger,
                backgroundColor: 'rgba(3, 189, 0, 0.3)',
                borderColor: "rgba(3, 189, 0, 0.4)",
                fill: false,
                stepped: true,
                pointRadius: 5,
                pointStyle: 'crossRot'
            },
            {
                label: "safety harness rate",
                data: this.datapoints.safety_harness,
                backgroundColor: 'rgba(31, 16, 232, 0.3)',
                borderColor: "rgba(31, 16, 232, 0.4)",
                fill: false,
                stepped: true,
                pointRadius: 5,
                pointStyle: 'rect'
            }  
        ]
        }
      }
    }
  }
  </script>