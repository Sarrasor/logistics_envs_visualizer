<template>
    <h2 class="mt-10 text-3xl font-medium text-gray-900 dark:text-white">Orders</h2>
    <div class="relative overflow-x-auto rounded-2xl shadow-xl max-h-dvh mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 bg-primary-200 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-3">
                        Id
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Client id
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Status
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Worker id
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Creation time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Assignment time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Pickup start time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Pickup end time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Drop off start time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Drop off end time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Completion time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Waiting time
                    </th>
                    <th scope="col" class="px-1 py-3">
                        Trip duration
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="order in orders" :key="order.id" class="bg-white border-t hover:bg-primary-50">
                    <th scope="row" class="px-4 py-1 font-bold text-gray-900 whitespace-nowrap ">
                        {{ order.id }}
                    </th>
                    <td class="px-1 py-2">
                        {{ order.client_id }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.status }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.assigned_worker_id || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.creation_time }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.assignment_time || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.pickup_start_time || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.pickup_end_time || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.drop_off_start_time || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.drop_off_end_time || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.completion_time || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ getWaitingTime(order) || "—" }}
                    </td>
                    <td class="px-1 py-2">
                        {{ getTripDurationTime(order) || "—" }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 p-2 bg-white">
        <PlotlyGraph :data="creationTimeData" :layout="creationTimeLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 p-2 bg-white">
        <PlotlyGraph :data="timeToAssignData" :layout="timeToAssignLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 p-2 bg-white">
        <PlotlyGraph :data="waitingTimeData" :layout="waitingTimeLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 p-2 bg-white">
        <PlotlyGraph :data="tripDurationData" :layout="tripDurationLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 bg-white">
        <p class="bg-white p-4 rounded-2xl text-center text-lg dark:bg-gray-800 dark:text-white">
            Orders from location distribution
        </p>
        <div class="relative overflow-x-auto rounded-2xl bg-white">
            <MapInfo :points="orderFromLocations"></MapInfo>
        </div>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 bg-white">
        <p class="bg-white p-4 rounded-2xl text-center text-lg dark:bg-gray-800 dark:text-white">
            Orders to location distribution
        </p>
        <div class="relative overflow-x-auto rounded-2xl bg-white">
            <MapInfo :points="orderToLocations"></MapInfo>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import PlotlyGraph from "./PlotlyGraph.vue"
import MapInfo from "./MapInfo.vue"

const histogramBins = 200

const creationTimeData = ref([{}])
const creationTimeLayout = ref({})

const timeToAssignData = ref([{}])
const timeToAssignLayout = ref({})

const waitingTimeData = ref([{}])
const waitingTimeLayout = ref({})

const tripDurationData = ref([{}])
const tripDurationLayout = ref({})

const orderFromLocations = ref([])
const orderToLocations = ref([])


const props = defineProps({
    orders: {
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

onMounted(() => {
    const orderCreationTimes = props.orders.map(order => order.creation_time)
    creationTimeData.value = [{
        x: orderCreationTimes,
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
    creationTimeLayout.value = {
        title: "Order creation times",
        xaxis: { title: "Creation time", range: [props.startTime, props.endTime] },
        yaxis: { title: "Count" },
        modebar: {
            orientation: 'v'
        }
    }

    const orderTimeToAssign = props.orders.flatMap(order => order.assignment_time ? order.assignment_time - order.creation_time : [])
    timeToAssignData.value = [{
        x: orderTimeToAssign,
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
    timeToAssignLayout.value = {
        title: "Order time to assign",
        xaxis: { title: "Time to assign" },
        yaxis: { title: "Count" },
        modebar: {
            orientation: 'v'
        }
    }

    const orderWaitingTimes = props.orders.flatMap(order => getWaitingTime(order) || [])
    waitingTimeData.value = [{
        x: orderWaitingTimes,
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
    waitingTimeLayout.value = {
        title: "Order waiting times",
        xaxis: { title: "Waiting time" },
        yaxis: { title: "Count" },
        modebar: {
            orientation: 'v'
        }
    }

    const orderTripDurations = props.orders.flatMap(order => getTripDurationTime(order) || [])
    tripDurationData.value = [{
        x: orderTripDurations,
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
    tripDurationLayout.value = {
        title: "Order trip durations",
        xaxis: { title: "Trip duration" },
        yaxis: { title: "Count" },
        modebar: {
            orientation: 'v'
        }
    }

    orderFromLocations.value = props.orders.map(order => {
        return {
            id: order.id,
            lat: order.from_location.lat,
            lon: order.from_location.lon
        }
    })

    orderToLocations.value = props.orders.map(order => {
        return {
            id: order.id,
            lat: order.to_location.lat,
            lon: order.to_location.lon
        }
    })
});


function getWaitingTime(order: Object) {
    if (order.pickup_start_time && order.creation_time) {
        return order.pickup_start_time - order.creation_time
    }
    return undefined
}

function getTripDurationTime(order: Object) {
    if (order.drop_off_start_time && order.pickup_end_time) {
        return order.drop_off_start_time - order.pickup_end_time
    }
    return undefined
}

</script>

<style scoped></style>