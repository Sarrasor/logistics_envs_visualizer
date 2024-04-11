<template>
    <aside id="logo-sidebar"
        class="fixed top-0 pt-14 left-0 z-40 w-96 h-screen transition-transform -translate-x-full bg-gray-100 border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700"
        aria-label="Sidebar">
        <div class="h-full px-3 pb-5 pt-3 overflow-y-auto">
            <RunDescription :frameData="frameData"></RunDescription>
            <WorkerTable :workers="frameData.observation.workers"></WorkerTable>
            <OrderTable :orders="frameData.observation.orders"></OrderTable>
        </div>
    </aside>
</template>

<script setup lang="ts">

import WorkerTable from './WorkerTable.vue'
import OrderTable from './OrderTable.vue'
import RunDescription from './RunDescription.vue'

const props = defineProps({
    frameData: {
        type: Object,
        required: true
    }
})
</script>