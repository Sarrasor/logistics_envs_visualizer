<template>
    <tr
        class="bg-white dark:bg-very-dark-gray-100 border-t hover:bg-primary-50 dark:hover:bg-very-dark-gray-50 dark:border-very-dark-gray-50">
        <td class="w-4 p-4">
            <div class="flex items-center">
                <input v-model="isSelected" id="checkbox-table-search-1" type="checkbox"
                    class="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-very-dark-gray-50 dark:border-gray-600">
                <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
            </div>
        </td>
        <th scope="row" class="px-6 py-4 font-bold text-gray-900 whitespace-nowrap dark:text-white">
            {{ runThumbnail.name }}
        </th>
        <td class="px-6 py-4">
            {{ formatDateTime(runThumbnail.creation_time) }}
        </td>
        <td class="px-6 py-4">
            <span class="mr-4">
                <span class="border font-medium rounded-2xl text-sm px-4 py-2 text-center"
                    :class="getStyleByStatus(runThumbnail.status)">
                    {{ runThumbnail.status }}
                </span>
            </span>
        </td>
        <td class="px-6 py-4 hover:text-primary-600 underline">
            <RouterLink :to="{ name: 'RunReport', params: { 'id': runThumbnail.id } }">
                View report
            </RouterLink>
        </td>
    </tr>
</template>


<script setup lang="ts">
import { ref } from "vue"
import { formatDateTime } from '../utils/common'

const props = defineProps({
    runThumbnail: Object
})

const isSelected = ref(false)

function getStyleByStatus(status: string) {
    var style = []
    if (status === "CREATED") {
        style = ["text-blue-500", "border-blue-500", "dark:text-blue-500", "dark:border-blue-500"]
    }
    else if (status === "RUNNING") {
        style = ["text-violet-500", "border-violet-500", "dark:text-violet-500", "dark:border-violet-500"]
    }
    else if (status === "COMPLETED") {
        style = ["text-green-500", "border-green-500", "dark:text-green-500", "dark:border-green-500"]
    }
    else if (status === "ERROR") {
        style = ["text-red-500", "border-red-500", "dark:text-red-500", "dark:border-red-500"]
    }

    return style
}

function getSelectedValue() {
    return isSelected.value
}

function getId() {
    return props.runThumbnail.id
}

defineExpose({
    getSelectedValue, getId
})

</script>

<style scoped></style>