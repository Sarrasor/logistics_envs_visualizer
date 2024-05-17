<template>
    <h2 class="mt-10 text-3xl font-medium text-gray-900 dark:text-white">Metrics</h2>
    <div class="grid w-full gap-6 md:grid-cols-4 sm:grid-cols-2">
        <div v-for="metric in metrics" :key="metric.name"
            class="sm:max-w-96 p-6 bg-white rounded-lg shadow-xl dark:bg-gray-800 dark:border-gray-700 transition ease-in-out delay-10 hover:-translate-y-1 hover:bg-primary-400 dark:hover:bg-primary-600 duration-500">
            <h5 class="mb-2 text-xl tracking-tight text-gray-900 dark:text-white">
                {{ metric.name }}
            </h5>
            <h2 class="mb-2 text-4xl font-semibold tracking-tight text-gray-900 dark:text-white">
                {{ getMetricValueString(metric) }}
            </h2>
        </div>
    </div>

</template>

<script setup lang="ts">
import { getMetricValueString } from "../utils/common"

defineProps({
    metrics: {
        type: Object,
        required: true
    }
})
</script>

<style scoped></style>