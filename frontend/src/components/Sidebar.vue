<template>
    <aside id="logo-sidebar"
        class="fixed top-0 left-0 z-40 w-80 h-screen pt-20 transition-transform -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700"
        aria-label="Sidebar">
        <div class="h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800">
            <div>
                <p>{{ frameData.info.simulation_id }}</p>
                <p>Time: {{ frameData.observation.current_time }}</p>
            </div>
            <div>
                Workers:
                <li v-for="worker in frameData.observation.workers" :key="worker.id">
                    {{ worker.id }} {{ worker.status }}
                </li>
            </div>
            <div>
                Orders:
                <li v-for="order in frameData.observation.orders" :key="order.id">
                    {{ order.id }} {{ order.status }}
                </li>
            </div>
        </div>
    </aside>
</template>

<script setup lang="ts">

const props = defineProps({
    frameData: {
        type: Object,
        required: true
    }
})
</script>