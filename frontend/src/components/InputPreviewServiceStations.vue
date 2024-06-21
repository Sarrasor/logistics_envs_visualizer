<template>
    <h2 class="text-2xl font-normal mb-4 dark:text-white">Service stations</h2>

    <div class="relative overflow-x-auto max-h-[65vh] rounded-2xl shadow-xl mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-100">
            <thead class="text-xs text-gray-700 dark:text-white bg-primary-200 dark:bg-very-dark-gray-200 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-4">
                        Service station id
                    </th>
                    <th scope="col" class="px-4 py-4">
                        Location lat
                    </th>
                    <th scope="col" class="px-4 py-4">
                        Location lon
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="service_station in serviceStations" :key="service_station.id"
                    class="bg-white dark:bg-very-dark-gray-100 border-t hover:bg-primary-50 dark:hover:bg-very-dark-gray-50 dark:border-very-dark-gray-50">
                    <th scope="row" class="px-4 py-4 font-bold text-gray-900 dark:text-white whitespace-nowrap">
                        {{ service_station.id }}
                    </th>
                    <td class="px-4 py-4">
                        {{ service_station.location.lat.toFixed(6) }}
                    </td>
                    <td class="px-4 py-4">
                        {{ service_station.location.lon.toFixed(6) }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">

defineProps({
    serviceStations: {
        type: Object,
        required: true
    },
})

</script>

<style scoped></style>