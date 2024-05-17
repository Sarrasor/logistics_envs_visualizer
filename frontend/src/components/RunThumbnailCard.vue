<template>
    <RouterLink :to="{ name: 'RunReport', params: { 'id': runThumbnail.id } }">
        <div
            class="max-w-m bg-white rounded-lg shadow-md dark:bg-gray-800 transition ease-in-out delay-10 hover:-translate-y-1 hover:bg-primary-100 dark:hover:bg-primary-900 duration-500">
            <div class="p-5">
                <h5 class="mb-4 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ runThumbnail.name }}
                </h5>

                <span class="mr-4">
                    <span class="border-2 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2"
                        :class="getStyleByStatus(runThumbnail.status)">
                        {{ runThumbnail.status }}
                    </span>
                </span>
            </div>
        </div>
    </RouterLink>
</template>


<script setup lang="ts">
defineProps({
    runThumbnail: Object
})

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


</script>

<style scoped></style>