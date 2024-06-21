<template>
    <div class="relative overflow-x-auto rounded-2xl shadow-xl max-h-dvh mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-100">
            <thead class="text-xs text-gray-700 dark:text-white bg-primary-200 dark:bg-very-dark-gray-50 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-4">
                        Order id
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Customer id
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Status
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Worker id
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Creation time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Assignment time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Pickup start time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Pickup end time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Drop off start time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Drop off end time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Completion time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Waiting time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Trip duration
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="order in orders" :key="order.id"
                    class="bg-white dark:bg-very-dark-gray-100 border-t hover:bg-primary-50 dark:hover:bg-very-dark-gray-50 dark:border-very-dark-gray-50">
                    <th scope="row" class="px-4 py-4 font-bold text-gray-900 dark:text-white whitespace-nowrap ">
                        {{ order.id }}
                    </th>
                    <td class="px-1 py-4">
                        {{ order.client_id }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.status }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.assigned_worker_id || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.creation_time }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.assignment_time || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.pickup_start_time || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.pickup_end_time || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.drop_off_start_time || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.drop_off_end_time || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.completion_time || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ getWaitingTime(order) || "—" }}
                    </td>
                    <td class="px-1 py-4">
                        {{ getTripDurationTime(order) || "—" }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 p-2 bg-white dark:bg-very-dark-gray-100">
        <PlotlyGraph :data="creationTimeData" :layout="creationTimeLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 p-2 bg-white dark:bg-very-dark-gray-100">
        <PlotlyGraph :data="timeToAssignData" :layout="timeToAssignLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 p-2 bg-white dark:bg-very-dark-gray-100">
        <PlotlyGraph :data="waitingTimeData" :layout="waitingTimeLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 p-2 bg-white dark:bg-very-dark-gray-100">
        <PlotlyGraph :data="tripDurationData" :layout="tripDurationLayout"></PlotlyGraph>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 bg-white dark:bg-very-dark-gray-100">
        <p class="bg-white p-4 rounded-2xl text-center text-base dark:bg-very-dark-gray-100 dark:text-white">
            Orders from location distribution
        </p>
        <div class="relative overflow-x-auto rounded-2xl bg-white">
            <MapInfo :points="orderFromLocations"></MapInfo>
        </div>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 bg-white dark:bg-very-dark-gray-100">
        <p class="bg-white p-4 rounded-2xl text-center text-base dark:bg-very-dark-gray-100 dark:text-white">
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
    const markerStyle = {
        color: "#a5b4fc",
        line: {
            color: "#6366f1",
            width: 1.0,
        }
    }
    const opacity = 0.8

    const orderCreationTimes = props.orders.map(order => order.creation_time)
    creationTimeData.value = [{
        autosize: true,
        x: orderCreationTimes,
        xbins: {
            start: props.startTime,
            end: props.endTime,
            size: (props.endTime - props.startTime) / histogramBins,
        },
        type: 'histogram',
        marker: markerStyle,
        opacity: opacity,
    }]
    creationTimeLayout.value = {
        title: "Order creation times",
        xaxis: { title: "Creation time", range: [props.startTime, props.endTime] },
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

    const orderTimeToAssign = props.orders.flatMap(order => order.assignment_time ? order.assignment_time - order.creation_time : [])
    timeToAssignData.value = [{
        x: orderTimeToAssign,
        type: 'histogram',
        marker: markerStyle,
        opacity: opacity,
    }]
    timeToAssignLayout.value = {
        title: "Order time to assign",
        xaxis: { title: "Time to assign" },
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

    const orderWaitingTimes = props.orders.flatMap(order => getWaitingTime(order) || [])
    waitingTimeData.value = [{
        x: orderWaitingTimes,
        type: 'histogram',
        marker: markerStyle,
        opacity: opacity,
    }]
    waitingTimeLayout.value = {
        title: "Order waiting times",
        xaxis: { title: "Waiting time" },
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

    const orderTripDurations = props.orders.flatMap(order => getTripDurationTime(order) || [])
    tripDurationData.value = [{
        x: orderTripDurations,
        type: 'histogram',
        marker: markerStyle,
        opacity: opacity,
    }]
    tripDurationLayout.value = {
        title: "Order trip durations",
        xaxis: { title: "Trip duration" },
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