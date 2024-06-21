<template>
    <div class="mx-auto bg-neutral-100 dark:bg-very-dark-gray-200 p-10 xl:m-10 xl:rounded-2xl xl:shadow-2xl">
        <div role="status" class="max-w-sm animate-pulse" v-if="isLoading">
            <div class="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[330px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[300px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]"></div>
        </div>

        <div class="grid grid-cols-1 gap-4" v-else>
            <h1 class="text-6xl font-normal dark:text-white">{{ runReport.description.name }}</h1>
            <RunDescription :run-id="runReport.id" :description="runReport.description" />
        </div>

        <h2 class="mt-12 text-3xl font-normal mb-4 dark:text-white">Results</h2>

        <div class="bg-white dark:bg-very-dark-gray-100 rounded-2xl shadow-xl mt-2 mb-6">
            <ul class="flex text-m font-bold text-center" id="results-tablist" role="tablist">
                <li class="w-full" role="presentation">
                    <button class="inline-block p-4 pl-8 pr-8 m-2 rounded-2xl" id="metrics-tab" type="button" role="tab"
                        aria-controls="metrics-tab-content" aria-selected="false">Metrics</button>
                </li>
                <li class="w-full" role="presentation">
                    <button class="inline-block p-4 pl-8 pr-8 m-2 rounded-2xl" id="orders-tab" type="button" role="tab"
                        aria-controls="orders-tab-content" aria-selected="false">Orders</button>
                </li>
                <li class="w-full" role="presentation">
                    <button class="inline-block p-4 pl-8 pr-8 m-2 rounded-2xl" id="workers-tab" type="button" role="tab"
                        aria-controls="workers-tab-content" aria-selected="false">Workers</button>
                </li>
                <li class="w-full" role="presentation">
                    <button class="inline-block p-4 pl-8 pr-8 m-2 rounded-2xl" id="service-stations-tab" type="button"
                        role="tab" aria-controls="service-stations-tab-content" aria-selected="false">Service
                        stations</button>
                </li>
            </ul>
        </div>

        <div id="results-tablist-content">
            <div class="hidden" id="metrics-tab-content" role="tabpanel" aria-labelledby="metrics-tab">
                <RunMetrics v-if="isComplete(runReport)" :metrics="runReport.metrics" />
            </div>

            <div class="hidden" id="orders-tab-content" role="tabpanel" aria-labelledby="orders-tab">
                <OrdersInfo v-if="isComplete(runReport)" :orders="runReport.orders" :startTime="runReport.start_time"
                    :endTime="runReport.end_time" />
            </div>

            <div class="hidden" id="workers-tab-content" role="tabpanel" aria-labelledby="workers-tab">
                <WorkersInfo v-if="isComplete(runReport)" :workers="runReport.workers" />
            </div>

            <div class="hidden" id="service-stations-tab-content" role="tabpanel"
                aria-labelledby="service-stations-tab">
                <ServiceStationsInfo v-if="isComplete(runReport)" :serviceStations="runReport.service_stations"
                    :startTime="runReport.start_time" :endTime="runReport.end_time" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { Tabs } from 'flowbite'
import type { TabsOptions, TabsInterface, TabItem } from 'flowbite'
import type { InstanceOptions } from 'flowbite'
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import RunDescription from "../components/RunDescription.vue"
import RunMetrics from "../components/RunMetrics.vue"
import OrdersInfo from "../components/OrdersInfo.vue"
import WorkersInfo from "../components/WorkersInfo.vue"
import ServiceStationsInfo from "../components/ServiceStationsInfo.vue"


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

    const tabsElement = document.getElementById('results-tablist')

    const tabElements: TabItem[] = [
        {
            id: 'metrics',
            triggerEl: document.querySelector('#metrics-tab'),
            targetEl: document.querySelector('#metrics-tab-content'),
        },
        {
            id: 'orders',
            triggerEl: document.querySelector('#orders-tab'),
            targetEl: document.querySelector('#orders-tab-content'),
        },
        {
            id: 'workers',
            triggerEl: document.querySelector('#workers-tab'),
            targetEl: document.querySelector('#workers-tab-content'),
        },
        {
            id: 'service-stations',
            triggerEl: document.querySelector('#service-stations-tab'),
            targetEl: document.querySelector('#service-stations-tab-content'),
        },
    ]

    const options: TabsOptions = {
        defaultTabId: 'metrics',
        activeClasses: 'font-semibold text-primary-500 bg-primary-200 hover:bg-primary-300',
        inactiveClasses: 'bg-gray-50 dark:bg-very-dark-gray-100 hover:bg-gray-100',
        onShow: () => {
            window.dispatchEvent(new Event('resize'))
        },
    }

    const instanceOptions: InstanceOptions = {
        id: 'results-tablist',
        override: true
    }

    const tabs: TabsInterface = new Tabs(tabsElement, tabElements, options, instanceOptions)

    tabs.show('metrics')
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
    return !isLoading.value && runReport.description.status === "COMPLETED"
}
</script>