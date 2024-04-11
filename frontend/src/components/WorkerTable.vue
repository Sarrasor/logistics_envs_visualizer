<template>
    <h2 class="mt-5 text-xl font-medium text-gray-900 dark:text-white">
        Workers
    </h2>

    <div class="relative overflow-x-auto rounded-2xl shadow-xl max-h-dvh mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 bg-primary-200 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-3">
                        Id
                    </th>
                    <th scope="col" class="px-4 py-3">
                        Status
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="worker in workers" :key="worker.id" class="bg-white border-t hover:bg-primary-50">
                    <th scope="row" class="px-4 py-2 font-bold text-gray-900 whitespace-nowrap ">
                        <p class="px-1 py-1 rounded-full text-center" :class="getTextColor(worker.color)"
                            :style="getWorkerIdStyleString(worker.color)">
                            {{ worker.id }}
                        </p>
                    </th>
                    <td class="px-4 py-1">
                        {{ worker.status }}
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