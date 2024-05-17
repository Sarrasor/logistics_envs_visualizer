<template>
    <div class="h-full px-3 pb-5 pt-3 overflow-y-auto bg-gray-100">
        <LiveRunDescription :frameData="frameData">
        </LiveRunDescription>
        <WorkerTable :workers="frameData.observation.workers"></WorkerTable>
        <OrderTable :orders="frameData.observation.orders"></OrderTable>
    </div>
</template>

<script setup lang="ts">

import WorkerTable from './WorkerTable.vue'
import OrderTable from './OrderTable.vue'
import LiveRunDescription from './LiveRunDescription.vue'

const props = defineProps({
    frameData: {
        type: Object,
        required: true
    }
})
</script>