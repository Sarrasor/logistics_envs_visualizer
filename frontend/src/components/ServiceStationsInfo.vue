<template>
    <h2 class="mt-10 text-3xl font-medium text-gray-900 dark:text-white">Service stations</h2>
    <div class="relative overflow-x-auto rounded-2xl shadow-xl max-h-dvh mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 bg-primary-200 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-3">
                        Id
                    </th>
                    <th scope="col" class="px-1 py-3">
                        N services
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="serviceStation in serviceStations" :key="serviceStation.id"
                    class="bg-white border-t hover:bg-primary-50">
                    <th scope="row" class="px-4 py-1 font-bold text-gray-900 whitespace-nowrap ">
                        {{ serviceStation.id }}
                    </th>
                    <td class="px-1 py-2">
                        {{ serviceStation.service_events.length }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 p-2 bg-white">
        <PlotlyGraph :data="visitTimeData" :layout="visitTimeLayout"></PlotlyGraph>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import PlotlyGraph from "./PlotlyGraph.vue"

const props = defineProps({
    serviceStations: {
        type: Object,
        required: true
    },
    startTime: {
        type: Number,
        required: true
    },
    endTime: {
        type: Number,
        required: true
    }
})

const histogramBins = 200

const visitTimeData = ref([{}])
const visitTimeLayout = ref({})



onMounted(() => {
    // TODO(dburakov): map all service stations
    const visitTimes = props.serviceStations[0].service_events.map(event => event[1])
    visitTimeData.value = [{
        x: visitTimes,
        xbins: {
            start: props.startTime,
            end: props.endTime,
            size: (props.endTime - props.startTime) / histogramBins,
        },
        type: 'histogram',
        marker: {
            color: "#a5b4fc",
            line: {
                color: "#6366f1",
                width: 1.0,
            }
        },
        opacity: 0.5,
    }]
    visitTimeLayout.value = {
        title: "Service stations visit times",
        xaxis: { title: "Visit time", range: [props.startTime, props.endTime] },
        yaxis: { title: "Count" },
        modebar: {
            orientation: 'v'
        }
    }
});

</script>

<style scoped></style>