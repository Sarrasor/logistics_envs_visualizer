<template>
    <h2 class="text-xl font-medium text-gray-900">Run description</h2>
    <dl class="bg-white px-4 py-1 shadow-xl rounded-2xl text-gray-900 divide-y divide-gray-200 mt-2">
        <div class="flex flex-col py-1">
            <dt class="mb-1 text-gray-500 ">Run id</dt>
            <dd class="font-semibold">{{ frameData.info.simulation_id }}</dd>
        </div>
        <div class="flex flex-col py-1">
            <dt class="mb-1 text-gray-500 ">Time</dt>
            <dd class="font-semibold">{{ frameData.observation.current_time }}/{{ frameData.info.end_time }}</dd>
        </div>
    </dl>
</template>

<script setup lang="ts">
defineProps({
    frameData: {
        type: Object,
        required: true
    },
})
</script>