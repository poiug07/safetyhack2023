<template>
    <div class="bg-white p-3 bg-white rounded-lg">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Summary of workers</h2>
      <div class="mx-auto max-w-7xl px-6 lg:px-8 py-5">
        <dl class="grid grid-cols-1 gap-x-8 gap-y-16 text-center lg:grid-cols-3">
          <div v-for="stat in stats" :key="stat.id" class="mx-auto flex max-w-xs flex-col gap-y-4">
            <dt class="text-base leading-7 text-gray-600">{{ stat.name }}</dt>
            <dd class="order-first text-3xl font-semibold tracking-tight text-gray-900 sm:text-5xl">{{ stat.value }}</dd>
          </div>
        </dl>
      </div>
    </div>
  </template>
  
  <script setup>
  const stats = [
    { id: 1, name: 'Total Reward', value: '30000' },
    { id: 2, name: 'Best Reward', value: '20000' },
    { id: 3, name: 'Worst Reward', value: '5000' },
  ]
  </script>
