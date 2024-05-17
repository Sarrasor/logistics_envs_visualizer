<template>
    <div class="flex h-screen" v-if="hasData">
        <div class="w-96 flex-none">
            <Sidebar :frame-data="frameData" />
        </div>
        <div class="flex-initial w-full">
            <Map ref="map" :frame-data="frameData" />
        </div>
    </div>

    <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6" v-else>
        <div class="mx-auto max-w-screen-sm text-center">
            <p class="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white">
                No live data
            </p>

        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"

import Sidebar from "../components/Sidebar.vue"
import Map from "../components/Map.vue"

const hasData = ref(false)
const map = ref()
const frameData = ref({ observation: { bounds: { min: { lat: 0.0, lon: 0.0 }, max: { lat: 1.0, lon: 1.0 } }, workers: [], orders: [] }, info: { "simulation_id": "" } })

const websocketConnection = new WebSocket("ws://localhost:8000/ws")

var simulationId = ""

onMounted(async () => {
    websocketConnection.onopen = function () {
        hasData.value = false
        console.log("Connected to websocket")
    }

    websocketConnection.onmessage = function (e) {
        hasData.value = true
        frameData.value = JSON.parse(e.data)
        if (simulationId != frameData.value.info.simulation_id) {
            simulationId = frameData.value.info.simulation_id
            map.value.updateData(frameData.value.observation.bounds)
        }
    }

    websocketConnection.onerror = function (e) {
        hasData.value = false
        console.log("Error in websocket connection:")
        console.log(e)
    }

})

</script>