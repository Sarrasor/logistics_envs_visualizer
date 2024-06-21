<template>
    <h2 class="text-2xl font-normal mb-4 dark:text-white">Orders</h2>

    <div class="relative overflow-x-auto max-h-[65vh] rounded-2xl shadow-xl mt-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-100">
            <thead class="text-xs text-gray-700 dark:text-white bg-primary-200 dark:bg-very-dark-gray-200 sticky top-0">
                <tr>
                    <th scope="col" class="px-4 py-4">
                        Order id
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Customer id
                    </th>
                    <th scope="col" class="px-1 py-4">
                        Creation time
                    </th>
                    <th scope="col" class="px-1 py-4">
                        From location lat
                    </th>
                    <th scope="col" class="px-1 py-4">
                        From location lon
                    </th>
                    <th scope="col" class="px-1 py-4">
                        To location lat
                    </th>
                    <th scope="col" class="px-1 py-4">
                        To location lon
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="order in orders" :key="order.id"
                    class="bg-white dark:bg-very-dark-gray-100 border-t hover:bg-primary-50 dark:hover:bg-very-dark-gray-50 dark:border-very-dark-gray-50">
                    <th scope="row" class="px-4 py-4 font-bold text-gray-900 dark:text-white whitespace-nowrap">
                        {{ order.id }}
                    </th>
                    <td class="px-1 py-4">
                        {{ order.client_id }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.creation_time }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.from_location.lat.toFixed(6) }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.from_location.lon.toFixed(6) }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.to_location.lat.toFixed(6) }}
                    </td>
                    <td class="px-1 py-4">
                        {{ order.to_location.lon.toFixed(6) }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">

defineProps({
    orders: {
        type: Object,
        required: true
    },
})

</script>

<style scoped></style>