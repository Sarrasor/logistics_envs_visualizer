<template>
    <h2 class="text-xl font-medium text-gray-900">Run description</h2>
    <dl class="bg-white px-4 py-1 shadow-xl rounded-2xl text-gray-900 divide-y divide-gray-200 mt-2">
        <div class="flex flex-col py-1">
            <dt class="mb-1 text-gray-500 ">Run id</dt>
            <dd class="font-semibold underline">
                <RouterLink :to="getRunLink(frameData.info.simulation_id)" target="_blank"
                    class="hover:text-primary-600">
                    {{ frameData.info.simulation_id }}
                </RouterLink>
            </dd>
        </div>
        <div class="flex flex-col py-1">
            <dt class="mb-1 text-gray-500 ">Time</dt>
            <dd class="font-semibold">{{ frameData.observation.current_time }}/{{ frameData.info.end_time }}</dd>
        </div>
        <div class="flex flex-col py-1" v-for="metric in frameData.info.metrics" :key="metric.name">
            <dt class="mb-1 text-gray-500 ">{{ metric.name }}</dt>
            <dd class="font-semibold"> {{ getMetricValueString(metric) }}</dd>
        </div>
    </dl>
</template>

<script setup lang="ts">
import { getMetricValueString } from "../utils/common"

defineProps({
    frameData: {
        type: Object,
        required: true
    },
})

function getRunLink(runId: string) {
    return `/runs/${runId}`
}
</script>