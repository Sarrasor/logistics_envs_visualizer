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

            <div class="flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between">
                <div>
                    <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio"
                        class="inline-flex items-center text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-2xl text-sm px-3 py-1.5 dark:bg-very-dark-gray-100 dark:text-white dark:border-gray-600 dark:hover:bg-very-dark-gray-50 dark:hover:border-gray-600 dark:focus:ring-gray-700"
                        type="button">
                        <svg class="w-4 h-4 text-primary-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                            fill="currentColor" viewBox="0 0 20 20">
                            <path
                                d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z" />
                        </svg>
                        <p class="min-w-32">{{ dateFilter }}</p>
                        <svg class="w-2.5 h-2.5 text-gray-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                            fill="none" viewBox="0 0 10 6">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 4 4 4-4" />
                        </svg>
                    </button>

                    <!-- Dropdown menu -->
                    <div id="dropdownRadio"
                        class="z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-2xl shadow"
                        data-popper-reference-hidden="" data-popper-escaped="" data-popper-placement="top"
                        style="position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 3847.5px, 0px);">
                        <ul class="p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200"
                            aria-labelledby="dropdownRadioButton">
                            <li>
                                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input @change="onDateFilter" checked id="filter-radio-example-1" type="radio"
                                        value="Last day" name="filter-radio"
                                        class="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                    <label for="filter-radio-example-1"
                                        class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last
                                        day</label>
                                </div>
                            </li>
                            <li>
                                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input @change="onDateFilter" id="filter-radio-example-2" type="radio"
                                        value="Last 7 days" name="filter-radio"
                                        class="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                    <label for="filter-radio-example-2"
                                        class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last
                                        7 days</label>
                                </div>
                            </li>
                            <li>
                                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input @change="onDateFilter" id="filter-radio-example-3" type="radio"
                                        value="Last 14 days" name="filter-radio"
                                        class="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                    <label for="filter-radio-example-3"
                                        class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last
                                        14 days</label>
                                </div>
                            </li>
                            <li>
                                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input @change="onDateFilter" id="filter-radio-example-4" type="radio"
                                        value="Last 30 days" name="filter-radio"
                                        class="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                    <label for="filter-radio-example-4"
                                        class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last
                                        30 days</label>
                                </div>
                            </li>
                            <li>
                                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input @change="onDateFilter" id="filter-radio-example-5" type="radio"
                                        value="Last 60 days" name="filter-radio"
                                        class="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                    <label for="filter-radio-example-5"
                                        class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last
                                        60 days</label>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>

                <button type="button" @click="onCompareRuns"
                    class="px-8 py-2 mt-2 mb-8 text-white bg-primary-400 hover:bg-primary-500 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Compare
                    runs
                </button>

                <label for="table-search" class="sr-only">Search</label>
                <div class="relative">
                    <div
                        class="absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none">
                        <svg class="w-5 h-5 text-gray-500 dark:text-white" aria-hidden="true" fill="currentColor"
                            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                clip-rule="evenodd"></path>
                        </svg>
                    </div>
                    <input type="text" @input="onSearch" id="table-search"
                        class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-2xl w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-very-dark-gray-100 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        placeholder="Search run by name">
                </div>
            </div>

            <div class="relative overflow-x-auto rounded-2xl shadow-2xl max-h-dvh mt-2">
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-100">
                    <thead
                        class="text-sm text-gray-700 dark:text-white bg-primary-200 dark:bg-very-dark-gray-50 sticky top-0">
                        <tr>
                            <!-- <th scope="col" class="p-4">
                                <div class="flex items-center">
                                    <input id="checkbox-all-search" type="checkbox"
                                        class="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-very-dark-gray-50 dark:border-gray-600">
                                    <label for="checkbox-all-search" class="sr-only">checkbox</label>
                                </div>
                            </th> -->
                            <th scope="col" class="px-6 py-4">
                                Compare
                            </th>
                            <th scope="col" class="px-6 py-4">
                                Run name
                            </th>
                            <th scope="col" class="px-6 py-4">
                                Date
                            </th>
                            <th scope="col" class="px-6 py-4">
                                Status
                            </th>
                            <th scope="col" class="px-6 py-4">
                                Report link
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <RunThumbnailCard v-for="runThumbnail in filteredThumbnails" :key="runThumbnail.id"
                            ref="thumbnailCards" :run-thumbnail="runThumbnail" />
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue"
import RunThumbnailCard from "../components/RunThumbnailCard.vue"
import { initDropdowns } from "flowbite";
import { useRouter } from "vue-router"

const runThumbnailList = ref([])
const thumbnailCards = ref([])
const isLoading = ref(true)
const router = useRouter()
const searchFilter = ref('')
const dateFilter = ref('Last day')

onMounted(async () => {
    const result = await fetch('/api/runs')
    const response = await result.json()
    runThumbnailList.value = response
    isLoading.value = false
    initDropdowns()
})

function onCompareRuns() {
    const runIds = thumbnailCards.value.filter(card => card.getSelectedValue()).map(card => card.getId())
    router.push({ name: 'RunComparison', query: { ids: runIds } })
}

const filteredThumbnails = computed(() => {
    let filteredList = runThumbnailList.value
    const secondsInDay = 24 * 60 * 60 * 1000
    console.log(dateFilter.value)
    if (dateFilter.value === 'Last day') {
        console.log("Filtering last day")
        filteredList = filteredList.filter(item => new Date(item.creation_time) > new Date(Date.now() - secondsInDay))
    } else if (dateFilter.value === 'Last 7 days') {
        filteredList = filteredList.filter(item => new Date(item.creation_time) > new Date(Date.now() - 7 * secondsInDay))
    } else if (dateFilter.value === 'Last 14 days') {
        filteredList = filteredList.filter(item => new Date(item.creation_time) > new Date(Date.now() - 14 * secondsInDay))
    } else if (dateFilter.value === 'Last 30 days') {
        filteredList = filteredList.filter(item => new Date(item.creation_time) > new Date(Date.now() - 30 * secondsInDay))
    } else if (dateFilter.value === 'Last 60 days') {
        filteredList = filteredList.filter(item => new Date(item.creation_time) > new Date(Date.now() - 60 * secondsInDay))
    }

    filteredList = filteredList.filter(item => item.name.toLowerCase().includes(searchFilter.value.toLowerCase()))

    filteredList = filteredList.sort((a, b) => new Date(b.creation_time) - new Date(a.creation_time))

    return filteredList
})

function onSearch(event) {
    searchFilter.value = event.target.value
}

function onDateFilter(event) {
    dateFilter.value = event.target.value
}
</script>