<script setup>
import SummaryRow from "./SummaryRow.vue";
import StepChart from "./StepChart.vue";
</script>

<template>
<div class="p-10 pt-5 bg-white rounded-lg">
    <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-3">Summary of workers</h2>
    <p class="text-gray-400 mb-4">Click on row to view more info.</p>
    <table class="min-w-full text-left text-m font-light">
        <thead class="border-b font-medium dark:border-neutral-500">
            <tr>
                <th>Worker</th>
                <th>PPE Absent</th>
                <th>Danger Zone</th>
                <th>Safety Harness</th>
            </tr>
        </thead>
        <tbody>
            <SummaryRow v-for="worker in workers" :key="worker" :worker_id="worker" @click="display(worker)"></SummaryRow>
        </tbody>
    </table>
    <div v-if="rewardsVisible" class="text-center text-base p-10">
        <p class="text-2xl font-bold">Reward for worker WXXXX{{ selectedWorker }}: <span class=" text-3xl text-indigo-600">{{ reward }}</span></p>

        <div class="mt-5">
            <StepChart :datapoints="chartdata"></StepChart>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            selectedWorker: 0,
            reward: 0,
            rewardsVisible: false,
            chartdata: {},
        }
    },
    methods: {
        async display(worker) {
            if (this.rewardsVisible && this.selectedWorker==worker) {
                this.rewardsVisible = false;
                return;
            }
            const response = await fetch(`http://localhost:8000/api/workers/${worker}/reward`);
            const reward = await response.json();
            this.selectedWorker = worker;
            this.reward = reward.reward;
            this.rewardsVisible = true;

            const pointsresp = await fetch(`http://localhost:8000/api/points/${worker}`);
            const points = await pointsresp.json();
            this.chartdata = points;
            console.log(this.chartdata);
        }
    },
}

const response = await fetch("http://localhost:8000/api/workers");
const workers = await response.json();
console.log(workers);
</script>
