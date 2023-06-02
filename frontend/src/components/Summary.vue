<script setup>
import { ref } from 'vue'

</script>

<template>
<div class="p-3 bg-white rounded-lg">
    <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Summary of workers</h2>
    <table class="min-w-full text-left text-m font-light">
        <thead class="border-b font-medium dark:border-neutral-500">
            <tr>
                <th>Worker</th>
                <th>PPE Absent</th>
                <th>Danger Zone</th>
                <th>Safety Harness</th>
            </tr>
  </thead>
  <tbody >
      <tr class="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
          <td>WXXX1</td>
          <td>Malcolm Lockyer</td>
          <td>1961</td>
          <td>1961</td>
        </tr>
        <tr class="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
            <td>WXXX2</td>
            <td>The Eagles</td>
            <td>1972</td>
            <td>1972</td>
        </tr>
        <tr class="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
            <td>WXXX3</td>
            <td>Earth, Wind, and Fire</td>
            <td>1975</td>
            <td>1975</td>
        </tr>
        <tr class="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
            <td>WXXX4</td>
            <td>Earth, Wind, and Fire</td>
            <td>1975</td>
            <td>1975</td>
        </tr>
        <tr class="border-b transition duration-300 ease-in-out hover:bg-neutral-100 dark:border-neutral-500 dark:hover:bg-neutral-600">
            <td>WXXX5</td>
            <td>Earth, Wind, and Fire</td>
            <td>1975</td>
            <td>1975</td>
        </tr>
    </tbody>
</table>
</div>
</template>

<style scoped>
</style>
