<script setup>
import SummaryRow from "./SummaryRow.vue";
import StepChart from "./StepChart.vue";
</script>

<template>
<div class="p-10 pt-5 bg-white rounded-lg">
    <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-3">Summary for each worker</h2>
    <p class="text-gray-400 mb-4">Click on row to view more info.</p>
    <table class="min-w-full text-left text-m font-light">
        <thead class="border-b font-medium dark:border-neutral-500">
            <tr>
                <th>Worker</th>
                <th>PPE Present</th>
                <th>Danger Zone</th>
                <th>Safety Harness</th>
            </tr>
        </thead>
        <tbody>
            <SummaryRow v-for="worker in workers" :key="worker" :worker_id="worker" @click="display(worker)"></SummaryRow>
        </tbody>
    </table>
    <div v-if="rewardsVisible" class="text-center text-base p-10">
        <p class="text-2xl font-bold">Reward for worker WXXX{{ selectedWorker }}: <span class=" text-3xl text-indigo-600">{{ reward }}</span></p>
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
            workers: [],
        }
    },
    methods: {
        async display(worker) {
            if (this.rewardsVisible && this.selectedWorker==worker) {
                this.rewardsVisible = false;
                return;
            }
            const response = await fetch(`https://e1fb-175-45-22-2.ngrok-free.app/api/workers/${worker}/reward`, {
      headers: {
        "ngrok-skip-browser-warning": "69420",
        "Content-Type": "application/json",
      },
      mode: 'cors'});
            const reward = await response.json();
            this.selectedWorker = worker;
            this.reward = reward.reward;
            this.rewardsVisible = true;

            const pointsresp = await fetch(`https://e1fb-175-45-22-2.ngrok-free.app/api/points/${worker}`, {
      headers: {
        "ngrok-skip-browser-warning": "69420",
        "Content-Type": "application/json",
      },
      mode: 'cors'});
            const points = await pointsresp.json();
            this.chartdata = points;
            console.log(this.chartdata);
        }
    },
    async mounted() {
        const response = await fetch("https://e1fb-175-45-22-2.ngrok-free.app/api/workers", {
        headers: {
            "ngrok-skip-browser-warning": "69420",
            "Content-Type": "application/json",
        },
        mode: 'cors'});
        this.workers = await response.json();
        console.log(this.workers);
    }
}
</script>
