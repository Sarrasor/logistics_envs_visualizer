<template>
    <div class="mx-auto bg-neutral-100 dark:bg-gray-900 p-10 xl:m-10 xl:rounded-2xl xl:shadow-2xl">
        <h1 class="text-3xl font-bold mb-8 dark:text-white">Specify your problem</h1>
        <form @submit.prevent="process">
            <div class="md:flex">
                <ul class="flex-column w-96 space-y space-y-5 text-sm font-normal text-gray-500 dark:text-gray-100 md:me-4 mb-4 md:mb-0"
                    id="problem-tablist" role="tablist">

                    <div class="mb-8">
                        <FileInput @update:model-value="onFile" ref="fileInput" v-model="inputFile"></FileInput>
                    </div>

                    <li role="presentation">
                        <a href="#" class="inline-flex items-center px-4 py-8 shadow-xl rounded-2xl w-full"
                            id="general-tab" type="button" role="tab" aria-controls="general-tab-content"
                            aria-selected="false">
                            <svg class="w-6 h-6 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24"
                                height="24" fill="currentColor" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-width="2"
                                    d="M20 6H10m0 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0m0 0H4m16 6h-2m0 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0m0 0H4m16 6H10m0 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0m0 0H4" />
                            </svg>

                            General
                        </a>
                    </li>

                    <li role="presentation">
                        <a href="#" class="inline-flex items-center px-4 py-8 shadow-xl rounded-2xl w-full" id="map-tab"
                            type="button" role="tab" aria-controls="map-tab-content" aria-selected="false">
                            <svg class="w-6 h-6 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24"
                                height="24" fill="currentColor" viewBox="0 0 24 24">
                                <path fill-rule="evenodd"
                                    d="M11.906 1.994a8.002 8.002 0 0 1 8.09 8.421 7.996 7.996 0 0 1-1.297 3.957.996.996 0 0 1-.133.204l-.108.129c-.178.243-.37.477-.573.699l-5.112 6.224a1 1 0 0 1-1.545 0L5.982 15.26l-.002-.002a18.146 18.146 0 0 1-.309-.38l-.133-.163a.999.999 0 0 1-.13-.202 7.995 7.995 0 0 1 6.498-12.518ZM15 9.997a3 3 0 1 1-5.999 0 3 3 0 0 1 5.999 0Z"
                                    clip-rule="evenodd" />
                            </svg>

                            Map
                        </a>
                    </li>

                    <li role="presentation">
                        <a href="#" class="inline-flex items-center px-4 py-8 shadow-xl rounded-2xl w-full"
                            id="orders-tab" type="button" role="tab" aria-controls="orders-tab-content"
                            aria-selected="false">

                            <svg class="w-6 h-6 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24"
                                height="24" fill="currentColor" viewBox="0 0 24 24">
                                <path fill-rule="evenodd"
                                    d="M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm-2 9a4 4 0 0 0-4 4v1a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-1a4 4 0 0 0-4-4h-4Z"
                                    clip-rule="evenodd" />
                            </svg>

                            Orders
                        </a>
                    </li>

                    <li role="presentation">
                        <a href="#" class="inline-flex items-center px-4 py-8 shadow-xl rounded-2xl w-full"
                            id="workers-tab" type="button" role="tab" aria-controls="workers-tab-content"
                            aria-selected="false">
                            <svg class="w-6 h-6 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24"
                                height="24" fill="currentColor" viewBox="0 0 24 24">
                                <path fill-rule="evenodd"
                                    d="M4 4a2 2 0 0 0-2 2v9a1 1 0 0 0 1 1h.535a3.5 3.5 0 1 0 6.93 0h3.07a3.5 3.5 0 1 0 6.93 0H21a1 1 0 0 0 1-1v-4a.999.999 0 0 0-.106-.447l-2-4A1 1 0 0 0 19 6h-5a2 2 0 0 0-2-2H4Zm14.192 11.59.016.02a1.5 1.5 0 1 1-.016-.021Zm-10 0 .016.02a1.5 1.5 0 1 1-.016-.021Zm5.806-5.572v-2.02h4.396l1 2.02h-5.396Z"
                                    clip-rule="evenodd" />
                            </svg>

                            Workers
                        </a>
                    </li>

                    <li role="presentation">
                        <a href="#" class="inline-flex items-center px-4 py-8 shadow-xl rounded-2xl w-full"
                            id="service-stations-tab" type="button" role="tab"
                            aria-controls="service-stations-tab-content" aria-selected="false">


                            <svg class="w-6 h-6 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24"
                                height="24" fill="currentColor" viewBox="0 0 24 24">
                                <path fill-rule="evenodd"
                                    d="M9.586 2.586A2 2 0 0 1 11 2h2a2 2 0 0 1 2 2v.089l.473.196.063-.063a2.002 2.002 0 0 1 2.828 0l1.414 1.414a2 2 0 0 1 0 2.827l-.063.064.196.473H20a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-.089l-.196.473.063.063a2.002 2.002 0 0 1 0 2.828l-1.414 1.414a2 2 0 0 1-2.828 0l-.063-.063-.473.196V20a2 2 0 0 1-2 2h-2a2 2 0 0 1-2-2v-.089l-.473-.196-.063.063a2.002 2.002 0 0 1-2.828 0l-1.414-1.414a2 2 0 0 1 0-2.827l.063-.064L4.089 15H4a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2h.09l.195-.473-.063-.063a2 2 0 0 1 0-2.828l1.414-1.414a2 2 0 0 1 2.827 0l.064.063L9 4.089V4a2 2 0 0 1 .586-1.414ZM8 12a4 4 0 1 1 8 0 4 4 0 0 1-8 0Z"
                                    clip-rule="evenodd" />
                            </svg>

                            Service stations
                        </a>
                    </li>
                </ul>

                <div class="p-6 bg-gray-50 dark:bg-very-dark-gray-100 text-medium rounded-2xl shadow-xl w-full"
                    id="default-tab-content">
                    <div class="hidden" id="general-tab-content" role="tabpanel" aria-labelledby="general-tab">
                        <h2 class="text-2xl font-normal mb-4 dark:text-white">General settings</h2>
                        <h3 class="mb-6 text-lg font-medium text-gray-900 dark:text-white">Select run name:</h3>
                        <div class="max-w-96">
                            <input v-model="runName" type="text" id="first_name"
                                class="bg-white border border-gray-300 text-gray-900 text-sm rounded-2xl focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-very-dark-gray-100 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="My run name (optional)" />
                        </div>

                        <h3 class="mt-8 text-lg font-medium text-gray-900 dark:text-white">Select logistics environment:
                        </h3>
                        <ul class="grid w-full gap-3 md:grid-cols-2">
                            <li>
                                <input v-model="logisticsEnvironment" type="radio" id="logistics-problem-q-commerce"
                                    name="logistics-problem" value="Q_COMMERCE" class="opacity-0 peer" required />
                                <label for="logistics-problem-q-commerce"
                                    class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-2xl cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                                    <div class="block">
                                        <div class="w-full text-lg font-semibold">Q Commerce</div>
                                        <div class="w-full">Online ultra-fast neighborhood delivery services</div>
                                    </div>
                                </label>
                            </li>
                            <li>
                                <input v-model="logisticsEnvironment" type="radio" id="logistics-problem-ride-hailing"
                                    name="logistics-problem" value="RIDE_HAILING" class="opacity-0 peer">
                                <label for="logistics-problem-ride-hailing"
                                    class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-2xl cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                                    <div class="block">
                                        <div class="w-full text-lg font-semibold">Ride Hailing</div>
                                        <div class="w-full">Taxi-like services</div>
                                    </div>
                                </label>
                            </li>
                        </ul>

                        <h3 class="mt-8 text-lg font-medium text-gray-900 dark:text-white">Select location mode:</h3>
                        <ul class="grid w-full gap-3 md:grid-cols-2">
                            <li>
                                <input v-model="locationMode" type="radio" id="location-mode-cartesian"
                                    name="location-mode" value="CARTESIAN" class="opacity-0 peer" required />
                                <label for="location-mode-cartesian"
                                    class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-2xl cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-very-dark-gray-100 dark:hover:bg-very-dark-gray-50">
                                    <div class="block">
                                        <div class="w-full text-lg font-semibold">Cartesian</div>
                                        <div class="w-full">Locations are constrained to be on a unit square <br> lat ∈
                                            [0.0,
                                            1.0], lon
                                            ∈ [0.0, 1.0]</div>
                                    </div>
                                </label>
                            </li>
                            <li>
                                <input v-model="locationMode" type="radio" id="location-mode-geographic"
                                    name="location-mode" value="GEOGRAPHIC" class="opacity-0 peer">
                                <label for="location-mode-geographic"
                                    class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-2xl cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-very-dark-gray-100 dark:hover:bg-very-dark-gray-50">
                                    <div class="block">
                                        <div class="w-full text-lg font-semibold">Geographic</div>
                                        <div class="w-full">Locations are valid geographic coordinates <br> lat ∈
                                            [-90.0,
                                            90.0], lon ∈
                                            [-180.0, 180.0]</div>
                                    </div>
                                </label>
                            </li>
                        </ul>

                        <h3 class="mt-8 text-lg font-medium text-gray-900 dark:text-white">Select run mode:</h3>
                        <ul class="grid w-full gap-3 md:grid-cols-2">
                            <li>
                                <input v-model="runMode" type="radio" id="run-mode-live" name="run-mode" value="LIVE"
                                    class="opacity-0 peer" required />
                                <label for="run-mode-live"
                                    class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-2xl cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-very-dark-gray-100 dark:hover:bg-very-dark-gray-50">
                                    <div class="block">
                                        <div class="w-full text-lg font-semibold">Live</div>
                                        <div class="w-full">Runs simulation in live mode</div>
                                    </div>
                                </label>
                            </li>
                            <li>
                                <input v-model="runMode" type="radio" id="run-mode-background" name="run-mode"
                                    value="BACKGROUND" class="opacity-0 peer">
                                <label for="run-mode-background"
                                    class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-2xl cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-very-dark-gray-100 dark:hover:bg-very-dark-gray-50">
                                    <div class="block">
                                        <div class="w-full text-lg font-semibold">Background</div>
                                        <div class="w-full">Runs simulation in background as fast as possible</div>
                                    </div>
                                </label>
                            </li>
                        </ul>
                    </div>

                    <div class="hidden" id="map-tab-content" role="tabpanel" aria-labelledby="map-tab">
                        <h2 class="text-2xl font-normal mb-4 dark:text-white">Map</h2>
                        <div class="relative overflow-x-auto rounded-2xl bg-white dark:bg-very-dark-gray-100">
                            <InputPreviewMap ref="map" :frame-data="validationResponse"></InputPreviewMap>
                        </div>
                    </div>

                    <div class="hidden" id="orders-tab-content" role="tabpanel" aria-labelledby="orders-tab">
                        <InputPreviewOrders :orders="validationResponse.observation.orders"></InputPreviewOrders>
                    </div>

                    <div class="hidden" id="workers-tab-content" role="tabpanel" aria-labelledby="workers-tab">
                        <InputPreviewWorkers :workers="validationResponse.observation.workers"></InputPreviewWorkers>
                    </div>

                    <div class="hidden" id="service-stations-tab-content" role="tabpanel"
                        aria-labelledby="service-stations-tab">
                        <InputPreviewServiceStations :serviceStations="validationResponse.observation.service_stations">
                        </InputPreviewServiceStations>
                    </div>
                </div>
            </div>

            <div v-if="!requestFailure" class="mt-6 text-right">
                <button v-if="!sendingRequest" type="submit"
                    class="text-white bg-primary-500 hover:bg-primary-500 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg shadow-lg text-sm px-16 py-4 text-center dark:bg-primary-500 dark:hover:bg-primary-600 dark:focus:ring-primary-700 inline-flex items-center">
                    Solve
                </button>
                <button v-else disabled type="button"
                    class="text-white bg-primary-400 focus:ring-4 focus:ring-primary-300 font-medium rounded-2xl text-sm px-5 py-2.5 text-center me-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 inline-flex items-center">
                    <svg aria-hidden="true" role="status" class="inline w-4 h-4 me-3 text-white animate-spin"
                        viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                            fill="#E5E7EB" />
                        <path
                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                            fill="currentColor" />
                    </svg>
                    Sending the request. Please hang on
                </button>
            </div>
            <div v-else class="mt-10 bg-red-300 p-4 rounded-2xl">
                <p class="font-bold">Failed request:</p> {{ requestFailureMessage }}
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Tabs } from 'flowbite'
import type { TabsOptions, TabsInterface, TabItem } from 'flowbite'
import type { InstanceOptions } from 'flowbite'
import axios from 'axios'
import { useRouter } from "vue-router"
import FileInput from "../components/FileInput.vue"
import InputPreviewMap from "../components/InputPreviewMap.vue"
import InputPreviewOrders from "../components/InputPreviewOrders.vue"
import InputPreviewWorkers from "../components/InputPreviewWorkers.vue"
import InputPreviewServiceStations from "../components/InputPreviewServiceStations.vue"


const router = useRouter()
const fileInput = ref(null)

const map = ref(null)
const runName = ref("")
const logisticsEnvironment = ref("RIDE_HAILING")
const locationMode = ref("GEOGRAPHIC")
const runMode = ref("LIVE")
const inputFile = ref(null)

const sendingRequest = ref(false)
const requestFailure = ref(false)
const requestFailureMessage = ref("")
const responseMessage = ref(null)


const validationResponse = ref({
    observation: {
        bounds: {
            "min": {
                "lat": 0.0,
                "lon": 1.0
            },
            "max": {
                "lat": 0.0,
                "lon": 1.0
            }
        },
        workers: [],
        orders: [],
        service_stations: [],
    },
})


onMounted(async () => {
    const tabsElement = document.getElementById('problem-tablist')

    const tabElements: TabItem[] = [
        {
            id: 'general',
            triggerEl: document.querySelector('#general-tab'),
            targetEl: document.querySelector('#general-tab-content'),
        },
        {
            id: 'map',
            triggerEl: document.querySelector('#map-tab'),
            targetEl: document.querySelector('#map-tab-content'),
        },
        {
            id: 'orders',
            triggerEl: document.querySelector('#orders-tab'),
            targetEl: document.querySelector('#orders-tab-content'),
        },
        {
            id: 'workers',
            triggerEl: document.querySelector('#workers-tab'),
            targetEl: document.querySelector('#workers-tab-content'),
        },
        {
            id: 'service-stations',
            triggerEl: document.querySelector('#service-stations-tab'),
            targetEl: document.querySelector('#service-stations-tab-content'),
        },
    ]

    const options: TabsOptions = {
        defaultTabId: 'general',
        activeClasses: 'font-semibold text-primary-500 bg-primary-200 hover:bg-primary-300',
        inactiveClasses: 'bg-gray-50 dark:bg-very-dark-gray-100 hover:bg-gray-100',
        onShow: () => {
            window.dispatchEvent(new Event('resize'))
            if (validationResponse.value.observation.bounds !== undefined) {
                map.value.updateData(validationResponse.value.observation.bounds)
            }
        },
    }

    const instanceOptions: InstanceOptions = {
        id: 'problem-tablist',
        override: true
    }

    const tabs: TabsInterface = new Tabs(tabsElement, tabElements, options, instanceOptions)

    tabs.show("general")
})

function process() {
    if (inputFile.value === null) {
        fileInput.value.invalidateForm()
        return
    }

    var formData = new FormData()
    formData.append("input_file", inputFile.value)
    formData.append("logistics_environment", logisticsEnvironment.value)
    formData.append("location_mode", locationMode.value)
    formData.append("run_mode", runMode.value)
    formData.append("run_name", runName.value)

    sendingRequest.value = true

    axios.post('/api/solve', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then(function (response) {
        responseMessage.value = response.data
        if (responseMessage.value.status === "FAILED_TO_CREATE") {
            requestFailure.value = true
            requestFailureMessage.value = responseMessage.value.message
            return
        }

        if (runMode.value === "LIVE") {
            router.push({ name: "LiveMonitor", params: {} })
        }
        else {
            router.push({ name: "RunReport", params: { id: response.data.run_id } })
        }
    }).catch(function () {
        requestFailure.value = true
        requestFailureMessage.value = "Failed to send the request. Maybe the server is down..."
    })
}

function onFile(fileEvent) {
    var formData = new FormData()
    formData.append("input_file", fileEvent)

    axios.post('/api/validate_input', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then(function (response) {
        validationResponse.value = response.data
        map.value.updateData(validationResponse.value.observation.bounds)
    }).catch(function () {
        console.log("Failed to validate")
    })
}
</script>