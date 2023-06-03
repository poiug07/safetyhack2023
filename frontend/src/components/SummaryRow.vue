<template>
    <tr class="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
        <td>WXXX{{ worker_id }}</td>
        <td>{{ ppe }}</td>
        <td>{{ danger }}</td>
        <td>{{ safety_harness }}</td>
    </tr>
</template>

<script>
import { onMounted } from 'vue';

export default {
    props: {
        worker_id: Number
    },
    data() {
        return {
            ppe: 0,
            danger: 0,
            safety_harness: 0 
        }
    },
    async mounted() {
        const response = await fetch(`https://e1fb-175-45-22-2.ngrok-free.app/api/sumstat/${this.worker_id}`, {
      headers: {
        "ngrok-skip-browser-warning": "69420",
        "Content-Type": "application/json",
      },
      mode: 'cors'});
        const data = await response.json();
        this.ppe = data.ppe;
        this.danger = data.danger;
        this.safety_harness = data.safety_harness;
    }
}
</script>