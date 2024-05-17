<template>
    <div class="mx-auto bg-neutral-100 dark:bg-gray-900 p-10 xl:m-10 xl:rounded-2xl xl:shadow-2xl">
        <div role="status" class="max-w-sm animate-pulse" v-if="isLoading">
            <div class="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[330px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[300px] mb-2.5"></div>
            <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]"></div>
        </div>

        <div class="grid grid-cols-1 gap-4" v-else>
            <h1 class="text-3xl font-bold dark:text-white">Runs</h1>
            <p v-if="runThumbnailList.length < 1" class="text-m">
                No runs were created yet. You can create a run
                <RouterLink to="/solve" class="underline">here
                </RouterLink>
            </p>

            <RunThumbnailCard v-for="runThumbnail in runThumbnailList" :key="runThumbnail.id"
                :run-thumbnail="runThumbnail" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import RunThumbnailCard from "../components/RunThumbnailCard.vue"

const runThumbnailList = ref([])
const isLoading = ref(true)

onMounted(async () => {
    const result = await fetch('/api/runs')
    const response = await result.json()
    runThumbnailList.value = response
    isLoading.value = false
})
</script>