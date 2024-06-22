<template>
    <l-polyline :lat-lngs="getPathPoints(worker.path, 0, worker.location)" color="rgb(120, 120, 120)" :weight=5
        :opacity=0.4></l-polyline>
    <l-polyline :lat-lngs="getPathPoints(worker.path, worker.remaining_path_index, worker.location)"
        :color="worker.color" :weight=5 :opacity=0.6></l-polyline>
    <l-marker :lat-lng="locationToList(worker.location)">
        <l-icon :icon-size="[10, 10]" :icon-anchor="[22, 43]" class-name="workerMarker">
            <div class="bg-gray-100 flex pe-10 ps-1 rounded-full">
                <div class="me-1 my-1.5 min-h-1 min-w-2 rounded-full" :class="getColorClass(worker)"></div>
                <div class="float font-bold self-center">{{ worker.id }}</div>
            </div>

            <svg :fill="worker.color" class="w-8 h-8 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                width="24" height="24" viewBox="0 0 24 24">
                <path fill-rule="evenodd"
                    d="M4 4a2 2 0 0 0-2 2v9a1 1 0 0 0 1 1h.535a3.5 3.5 0 1 0 6.93 0h3.07a3.5 3.5 0 1 0 6.93 0H21a1 1 0 0 0 1-1v-4a.999.999 0 0 0-.106-.447l-2-4A1 1 0 0 0 19 6h-5a2 2 0 0 0-2-2H4Zm14.192 11.59.016.02a1.5 1.5 0 1 1-.016-.021Zm-10 0 .016.02a1.5 1.5 0 1 1-.016-.021Zm5.806-5.572v-2.02h4.396l1 2.02h-5.396Z"
                    clip-rule="evenodd" />
            </svg>

            <!-- <svg :fill="worker.color" class="w-8 h-8" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24"
                height="24" viewBox="0 0 24 24">
                <path fill-rule="evenodd"
                    d="M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm-2 9a4 4 0 0 0-4 4v1a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-1a4 4 0 0 0-4-4h-4Z"
                    clip-rule="evenodd" />
            </svg> -->
        </l-icon>
        <l-popup :content="workerPopup(worker)"></l-popup>
    </l-marker>
</template>


<script setup lang="ts">
import {
    LMarker,
    LIcon,
    LPopup,
    LPolyline,
} from "@vue-leaflet/vue-leaflet"
import { decode } from "google-polyline"
import { Location, locationToList, WorkerObservation } from "../utils/common"

defineProps({
    worker: {
        type: Object,
        required: true
    },
})

function getPathPoints(encoded_path: string, remainingPathIndex: number, currentLocation: Location) {
    if (!encoded_path) {
        return []
    }

    const decoded_path = decode(encoded_path)
    if (remainingPathIndex != 0) {
        return [[currentLocation.lat, currentLocation.lon]].concat(decoded_path.slice(remainingPathIndex))
    }

    return decoded_path
}

function workerPopup(worker: WorkerObservation) {
    const fuelPercentage = (100.0 * worker.fuel).toFixed(2)
    return "<h1><b>Worker</b></h1><br>" +
        `<b>Id:</b> ${worker.id}<br>` +
        `<b>Location:</b> ${worker.location.lat.toFixed(6)}, ${worker.location.lon.toFixed(6)}</br>` +
        `<b>Fuel:</b> ${fuelPercentage}%<br>` +
        `<b>Status:</b> ${worker.status}<br>`
}


function getColorClass(worker) {
    var color = "bg-gray-500"
    if (worker.status == "IDLE") {
        color = "bg-yellow-500"
    }
    else if (worker.status == "MOVING") {
        color = "bg-pink-500"
    }
    else if (worker.status == "MOVING_TO_SERVICE") {
        color = "bg-orange-500"
    }
    else if (worker.status == "IN_SERVICE") {
        color = "bg-orange-500"
    }
    else if (worker.status == "MOVING_TO_PICKUP") {
        color = "bg-blue-600"
    }
    else if (worker.status == "PICKING_UP") {
        color = "bg-blue-600 animate-pulse"
    }
    else if (worker.status == "MOVING_TO_DROP_OFF") {
        color = "bg-green-500"
    }
    else if (worker.status == "DROPPING_OFF") {
        color = "bg-green-500 animate-pulse"
    }

    const bgString = "min-h-2 min-w-2 " + color
    return bgString
}

</script>