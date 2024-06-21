<template>
    <div class="relative overflow-x-auto rounded-2xl shadow-xl max-h-dvh mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-100">
            <thead class="text-xs text-gray-700 dark:text-white bg-primary-200 dark:bg-very-dark-gray-50 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-4">
                        Service station id
                    </th>
                    <th scope="col" class="px-1 py-4">
                        N services
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="serviceStation in serviceStations" :key="serviceStation.id"
                    class="bg-white dark:bg-very-dark-gray-100 border-t hover:bg-primary-50 dark:hover:bg-very-dark-gray-50 dark:border-very-dark-gray-50">
                    <th scope="row" class="px-4 py-4 font-bold text-gray-900 dark:text-white whitespace-nowrap ">
                        {{ serviceStation.id }}
                    </th>
                    <td class="px-1 py-4">
                        {{ serviceStation.service_events.length }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 p-2 bg-white dark:bg-very-dark-gray-100">
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
    const markerStyle = {
        color: "#a5b4fc",
        line: {
            color: "#6366f1",
            width: 1.0,
        }
    }
    const opacity = 0.8

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
        marker: markerStyle,
        opacity: 0.8,
    }]
    visitTimeLayout.value = {
        title: "Service station visit times",
        xaxis: { title: "Visit time", range: [props.startTime, props.endTime] },
        yaxis: { title: "Count" },
        modebar: {
            orientation: 'v'
        },
        plot_bgcolor: "#FFFFFF",
        paper_bgcolor: "#FFFFFF",
        font: {
            color: 'black',
            family: 'Roboto'
        },
    }
});

</script>

<style scoped></style>