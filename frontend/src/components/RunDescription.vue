<template>
    <h2 class="mt-5 text-3xl font-medium text-gray-900 dark:text-white">Description</h2>
    <dl
        class="bg-white p-5 shadow-xl rounded-2xl text-gray-900 divide-y divide-gray-200 dark:text-white dark:divide-gray-700 dark:bg-gray-800">
        <div class="flex flex-col py-3">
            <dt class="mb-1 text-gray-500 md:text-lg dark:text-gray-400">Creation time</dt>
            <dd class="text-lg font-semibold">{{ formatDateTime(description.creation_time) }}</dd>
        </div>
        <div class="flex flex-col py-3">
            <dt class="mb-1 text-gray-500 md:text-lg dark:text-gray-400">Status</dt>
            <dd class="text-lg font-semibold">{{ getStatusText(description) }}</dd>
        </div>
        <div class="flex flex-col py-3">
            <dt class="mb-1 text-gray-500 md:text-lg dark:text-gray-400">Logistics environment</dt>
            <dd class="text-lg font-semibold">{{ description.logistics_environment }}</dd>
        </div>
        <div class="flex flex-col py-3">
            <dt class="mb-1 text-gray-500 md:text-lg dark:text-gray-400">Location mode</dt>
            <dd class="text-lg font-semibold">{{ description.location_mode }}</dd>
        </div>
    </dl>
</template>

<script setup lang="ts">
import { formatDateTime } from "../utils/common"
defineProps({
    runId: {
        type: String,
        required: true
    },
    description: {
        type: Object,
        required: true
    }
})

function getStatusText(runDescription: Object) {
    if (runDescription.status === "ERROR") {
        return `${runDescription.status}: ${runDescription.message}`
    }

    return runDescription.status
}
</script>

<style scoped></style>