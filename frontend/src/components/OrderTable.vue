<template>
    <h2 class="mt-5 text-xl font-medium text-gray-900 dark:text-white">
        Orders
    </h2>

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
                        Creation time
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="order in orders" :key="order.id" class="bg-white border-t hover:bg-primary-50">
                    <th scope="row" class="px-4 py-1 font-bold text-gray-900 whitespace-nowrap ">
                        {{ order.id }}
                    </th>
                    <td class="px-1 py-1">
                        {{ order.client_id }}
                    </td>
                    <td class="px-1 py-1">
                        {{ order.status }}
                    </td>
                    <td class="px-1 py-1">
                        {{ order.creation_time }}
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