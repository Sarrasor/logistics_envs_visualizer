<template>
    <div class="flex h-screen">
        <div class="w-96 flex-none">
            <Sidebar :frame-data="frameData" />
        </div>
        <div class="flex-initial w-full">
            <Map ref="map" :frame-data="frameData" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"

import Sidebar from "../components/Sidebar.vue"
import Map from "../components/Map.vue"

const map = ref()
const frameData = ref({ observation: { bounds: { min: { lat: 0.0, lon: 0.0 }, max: { lat: 1.0, lon: 1.0 } }, workers: [], orders: [] }, info: { "simulation_id": "" } })

const websocketConnection = new WebSocket("ws://localhost:8000/ws")

var simulationId = ""

onMounted(async () => {
    websocketConnection.onopen = function () {
        console.log("Connected to websocket")
    }

    websocketConnection.onmessage = function (e) {
        frameData.value = JSON.parse(e.data)
        if (simulationId != frameData.value.info.simulation_id) {
            simulationId = frameData.value.info.simulation_id
            map.value.updateData(frameData.value.observation.bounds)
        }
    }

    websocketConnection.onerror = function (e) {
        console.log("Error in websocket connection:")
        console.log(e)
    }

})

</script>