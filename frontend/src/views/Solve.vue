<template>
    <div class="mx-auto bg-neutral-100 dark:bg-gray-900 p-10 xl:m-10 xl:rounded-2xl xl:shadow-2xl">
        <h1 class="text-3xl font-bold mb-8 dark:text-white">Specify your problem</h1>
        <form @submit.prevent="process">
            <h3 class="mb-3 text-lg font-medium text-gray-900 dark:text-white">Select run name:</h3>
            <div class="max-w-96">
                <input v-model="runName" type="text" id="first_name"
                    class="bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                    placeholder="My run name (optional)" />
            </div>

            <h3 class="mt-8 text-lg font-medium text-gray-900 dark:text-white">Select logistics environment:</h3>
            <ul class="grid w-full gap-3 md:grid-cols-2">
                <li>
                    <input v-model="logisticsEnvironment" type="radio" id="logistics-problem-q-commerce"
                        name="logistics-problem" value="Q_COMMERCE" class="opacity-0 peer" required />
                    <label for="logistics-problem-q-commerce"
                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
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
                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
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
                    <input v-model="locationMode" type="radio" id="location-mode-cartesian" name="location-mode"
                        value="CARTESIAN" class="opacity-0 peer" required />
                    <label for="location-mode-cartesian"
                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                        <div class="block">
                            <div class="w-full text-lg font-semibold">Cartesian</div>
                            <div class="w-full">Locations are constrained to be on a unit square lat ∈ [0.0, 1.0], lon
                                ∈ [0.0, 1.0]</div>
                        </div>
                    </label>
                </li>
                <li>
                    <input v-model="locationMode" type="radio" id="location-mode-geographic" name="location-mode"
                        value="GEOGRAPHIC" class="opacity-0 peer">
                    <label for="location-mode-geographic"
                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                        <div class="block">
                            <div class="w-full text-lg font-semibold">Geographic</div>
                            <div class="w-full">Locations are valid coordinates lat ∈ [-90.0, 90.0], lon ∈ [-180.0,
                                180.0]</div>
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
                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                        <div class="block">
                            <div class="w-full text-lg font-semibold">Live</div>
                            <div class="w-full">Runs simulation in live mode</div>
                        </div>
                    </label>
                </li>
                <li>
                    <input v-model="runMode" type="radio" id="run-mode-background" name="run-mode" value="BACKGROUND"
                        class="opacity-0 peer">
                    <label for="run-mode-background"
                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-500 peer-checked:text-primary-500 hover:text-gray-600 hover:bg-primary-100 hover:border-primary-300 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
                        <div class="block">
                            <div class="w-full text-lg font-semibold">Background</div>
                            <div class="w-full">Runs simulation in background as fast as possible</div>
                        </div>
                    </label>
                </li>
            </ul>

            <h3 class="mt-8 mb-3 text-lg font-medium text-gray-900 dark:text-white">Select problem description file:
            </h3>
            <FileInput ref="fileInput" v-model="inputFile"></FileInput>

            <div v-if="!requestFailure" class="mt-10">
                <button v-if="!sendingRequest" type="submit"
                    class="text-white bg-primary-400 hover:bg-primary-500 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-10 py-2.5 text-center me-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 inline-flex items-center">
                    Solve
                </button>
                <button v-else disabled type="button"
                    class="text-white bg-primary-400 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 inline-flex items-center">
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
            <div v-else class="mt-10 bg-red-300 p-4 rounded-lg">
                <p class="font-bold">Failed request:</p> {{ requestFailureMessage }}
            </div>

        </form>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from "vue-router"
import FileInput from "../components/FileInput.vue"


const router = useRouter()
const fileInput = ref(null)

const runName = ref("")
const logisticsEnvironment = ref("RIDE_HAILING")
const locationMode = ref("GEOGRAPHIC")
const runMode = ref("LIVE")
const inputFile = ref(null)

const sendingRequest = ref(false)
const requestFailure = ref(false)
const requestFailureMessage = ref("")
const responseMessage = ref(null)

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

        // router.push({ name: "RunReport", params: { id: response.data.run_id } })
        router.push({ name: "LiveMonitor", params: {} })
    }).catch(function () {
        requestFailure.value = true
        requestFailureMessage.value = "Failed to send the request. Maybe the server is down..."
    })

}
</script>