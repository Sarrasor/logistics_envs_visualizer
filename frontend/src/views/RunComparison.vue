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

        <div v-else>
            <h1 class="text-3xl font-normal dark:text-white mb-6">Run comparison</h1>

            <div class="relative overflow-x-auto rounded-2xl shadow-xl mt-2">
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-100">
                    <thead
                        class="text-sm text-gray-700 dark:text-white bg-primary-200 dark:bg-very-dark-gray-50 sticky top-0">
                        <tr>
                            <th v-for="runName in comparisonFrame.metrics_table.column_names" :key="runName" scope="col"
                                class="px-4 py-4">
                                {{ runName }}
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="row in comparisonFrame.metrics_table.rows" :key="row.name"
                            class="bg-white dark:bg-very-dark-gray-100 border-t hover:bg-primary-50 dark:hover:bg-very-dark-gray-50 dark:border-very-dark-gray-50">
                            <th scope="row" class="px-4 py-4">
                                {{ row.name }}{{ formatUnit(row.unit) }}
                            </th>
                            <td v-for="data in row.data" class="px-4 py-4"
                                :class="data.best ? 'font-bold text-primary-400 dark:text-primary-500' : ''">
                                {{ formatValue(data.value) }}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div v-for="plot in comparisonFrame.plots" :key="plot.layout.title"
                class="relative overflow-x-auto rounded-2xl shadow-xl mt-6 p-2 bg-white dark:bg-very-dark-gray-100">
                <PlotlyGraph :data="plot.data" :layout="plot.layout"></PlotlyGraph>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import PlotlyGraph from "../components/PlotlyGraph.vue"
import { useRouter } from "vue-router"

const isLoading = ref(true)
const comparisonFrame = ref(null)
const router = useRouter()

onMounted(async () => {
    const ids = router.currentRoute.value.query.ids
    const result = await fetch(`/api/compare?ids=${ids}`)

    if (result.status == 404) {
        router.push({ name: "NotFound" })
    }

    const response = await result.json()
    comparisonFrame.value = response
    console.log(comparisonFrame.value)

    isLoading.value = false
})

function formatValue(value: number) {
    var value_string = ""
    if (value % 1 != 0) {
        value_string += value.toFixed(2)
    }
    else {
        value_string += value
    }
    return value_string
}

function formatUnit(unit: string) {
    if (unit != "") {
        return " (" + unit + ")"
    }
    return ""
}
</script>