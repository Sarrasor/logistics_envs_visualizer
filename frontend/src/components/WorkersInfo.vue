<template>
    <div class="relative overflow-x-auto rounded-2xl shadow-xl max-h-dvh mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 bg-primary-200 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-4">
                        Id
                    </th>
                    <th scope="col" class="px-4 py-4">
                        Travel type
                    </th>
                    <th scope="col" class="px-4 py-4">
                        N assigned orders
                    </th>
                    <th scope="col" class="px-4 py-4">
                        N completed orders
                    </th>
                    <th scope="col" class="px-4 py-4">
                        Completion rate (%)
                    </th>
                    <th scope="col" class="px-4 py-4">
                        Idle rate (%)
                    </th>
                    <th scope="col" class="px-4 py-4">
                        With order rate (%)
                    </th>
                    <th scope="col" class="px-4 py-4">
                        Travel distance (km)
                    </th>
                    <th scope="col" class="px-4 py-4">
                        Total fuel consumption (%)
                    </th>
                    <th scope="col" class="px-4 py-4">
                        N service station visits
                    </th>

                </tr>
            </thead>
            <tbody>
                <tr v-for="worker in workers" :key="worker.id" class="bg-white border-t hover:bg-primary-50">
                    <th scope="row" class="px-4 py-4 font-bold text-gray-900 whitespace-nowrap ">
                        <p class="px-10 py-2 rounded-full text-center max-w-fit" :class="getTextColor(worker.color)"
                            :style="getWorkerIdStyleString(worker.color)">
                            {{ worker.id }}
                        </p>
                    </th>
                    <td class="px-4 py-4">
                        {{ worker.travel_type }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.n_assigned_orders }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.n_completed_orders }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.completion_rate.toFixed(2) }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.idle_rate.toFixed(2) }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.with_order_rate.toFixed(2) }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.traveled_distance.toFixed(2) }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.consumed_fuel.toFixed(2) }}
                    </td>
                    <td class="px-4 py-4">
                        {{ worker.n_service_station_visits }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">

import { isBright } from "../utils/common"

defineProps({
    workers: {
        type: Object,
        required: true
    },
})

function getTextColor(color: string) {
    return [isBright(color) ? "text-black" : "text-white"]
}

function getWorkerIdStyleString(color: string) {
    return `background-color: ${color};`
}

</script>

<style scoped></style>