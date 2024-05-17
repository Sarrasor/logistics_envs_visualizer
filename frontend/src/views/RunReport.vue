<template>
    <div class="mx-auto bg-neutral-100 dark:bg-gray-900 p-10 xl:m-10 xl:rounded-2xl xl:shadow-2xl">
        <div role="status" class="max-w-sm animate-pulse" v-if="isLoading">
            <div class="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[330px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[300px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]"></div>
        </div>

        <div class="grid grid-cols-1 gap-4" v-else>
            <h1 class="text-6xl font-bold dark:text-white">{{ runReport.description.name }}</h1>
            <RunDescription :run-id="runReport.id" :description="runReport.description" />
            <RunMetrics v-if="isComplete(runReport)" :metrics="runReport.metrics" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import RunDescription from "../components/RunDescription.vue"
import RunMetrics from "../components/RunMetrics.vue"


const props = defineProps({
    id: {
        type: String,
        required: true
    }
})

const runReport = ref()
const isLoading = ref(true)
const router = useRouter()

const reportRequestRetryTime = 5000


onMounted(async () => {
    getRunReport()
})

async function getRunReport() {
    const result = await fetch(`/api/runs/${props.id}`)
    if (result.status == 404) {
        router.push({ name: "NotFound" })
    }
    const response = await result.json()
    runReport.value = response
    isLoading.value = false

    if (!["COMPLETED", "ERROR"].includes(runReport.value.description.status)) {
        setTimeout(getRunReport, reportRequestRetryTime)
    }
}

function isComplete(runReport: Object) {
    return runReport.description.status === "COMPLETED"
}
</script>