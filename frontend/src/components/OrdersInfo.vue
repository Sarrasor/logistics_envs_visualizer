<template>
    <h2 class="mt-10 text-3xl font-medium text-gray-900 dark:text-white">Orders</h2>
    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2">
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
                        {{ order.assigned_worker_id }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.creation_time }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.assignment_time }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.pickup_start_time }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.pickup_end_time }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.drop_off_start_time }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.drop_off_end_time }}
                    </td>
                    <td class="px-1 py-2">
                        {{ order.completion_time }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2 p-2 bg-white">
        <PlotlyGraph :data="data" :layout="layout"></PlotlyGraph>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import PlotlyGraph from "./PlotlyGraph.vue"

const data = ref([{}])

const layout = {
    title: "Order creation times",
    xaxis: { title: "Creation time" },
    yaxis: { title: "Count" },
    modebar: {
        orientation: 'v'
    }
}

const props = defineProps({
    orders: {
        type: Object,
        required: true
    }
})

onMounted(() => {
    const orderCreationTimes = props.orders.map(order => order.creation_time)
    console.log(orderCreationTimes)
    data.value = [{
        x: orderCreationTimes,
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
});

</script>

<style scoped></style>